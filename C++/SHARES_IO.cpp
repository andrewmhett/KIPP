#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <cstring>

using namespace std;

map<string, unsigned int> accounts;

#pragma pack(push, 1)
struct Account{
	string id;
	unsigned int num_shares;
};
struct StoredAccount{
	char id[5];
	unsigned int num_shares;
};
#pragma pack(pop)

void map_data(string user_id){
	ifstream input;
	string KIPP_PATH;
	KIPP_PATH=getenv("KIPP_DIR");
	input.open(KIPP_PATH+"/C++/SHARES/"+user_id+".bin", ios::binary);
	vector<Account> accounts_v;
	char char_buf;
	while (input >> char_buf){
		input.putback(char_buf);
		StoredAccount read_struct;
		input.read(reinterpret_cast<char*>(&read_struct),sizeof(StoredAccount));
		Account new_struct;
		string id_str(read_struct.id);
		new_struct.id=id_str;
		new_struct.num_shares=read_struct.num_shares;
		accounts_v.push_back(new_struct);
	}
	input.close();
	for(vector<Account>::iterator it = accounts_v.begin(); it != accounts_v.end(); ++it){
		Account account = *it;
		accounts[account.id]=account.num_shares;
	}
}
void write_data(string user_id){
	string KIPP_PATH;
	KIPP_PATH=getenv("KIPP_DIR");
	ofstream output;
	output.open(KIPP_PATH+"/C++/SHARES/"+user_id+".bin", ios::binary);
	for (map<string, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
		StoredAccount write_struct;
		pair<string, unsigned int> account;
		account.first=it->first;
		account.second=it->second;
		strcpy(write_struct.id,account.first.c_str());
		write_struct.num_shares = account.second;
		output.write(reinterpret_cast<char*>(&write_struct),sizeof(StoredAccount));
	}
	output.close();
}
void edit_num_shares(string id, int num_shares){
	accounts[id] = num_shares;
	cout << id << " (number of shares): " << num_shares << endl;
}
void read_data(string id){
	if (id=="all"){
		for (map<string, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
			pair<string, unsigned int> account;
			account.first = it->first;
			account.second=it->second;
			cout << account.first << ": " << flush;
			cout << account.second << endl;
		}
	}else{
		cout << accounts[id] << endl;
	}
}
int main(int argc, const char * argv[]){
	string command=argv[2];
	string KIPP_PATH;
	KIPP_PATH=getenv("KIPP_DIR");
	command="sudo touch "+KIPP_PATH+"/C++/SHARES/"+command+".bin";
	system(command.c_str());
	map_data(argv[2]);
	if (*argv[1] == 'r'){
		if (strcmp(argv[3],"a")==0){
			read_data("all");
		}else{
			read_data(argv[3]);
		}
	}
	if (strcmp(argv[1],"wn")==0){
		edit_num_shares(argv[3], stoi(argv[4]));
	}
	write_data(argv[2]);
	return 0;
}
