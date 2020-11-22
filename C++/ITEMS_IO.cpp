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
	unsigned long item_data;
};
struct StoredAccount{
	char id[19];
	unsigned long item_data;
};
#pragma pack(pop)

void map_data(){
	ifstream input;
	string KIPP_PATH;
	KIPP_PATH=getenv("KIPP_DIR");
	input.open(KIPP_PATH+"/C++/ITEMS.bin", ios::binary);
	vector<Account> accounts_v;
	char char_buf;
	while (input >> char_buf){
		input.putback(char_buf);
		StoredAccount read_struct;
		input.read(reinterpret_cast<char*>(&read_struct),sizeof(StoredAccount));
		Account new_struct;
		string id_str(read_struct.id);
		new_struct.id=id_str;
		new_struct.item_data=read_struct.item_data;
		accounts_v.push_back(new_struct);
	}
	input.close();
	for(vector<Account>::iterator it = accounts_v.begin(); it != accounts_v.end(); ++it){
		Account account = *it;
		accounts[account.id] = account.item_data;
	}
}
void write_data(){
	string KIPP_PATH;
	KIPP_PATH=getenv("KIPP_DIR");
	ofstream output;
	output.open(KIPP_PATH+"/C++/ITEMS.bin", ios::binary);
	for (map<string, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
		StoredAccount write_struct;
		pair<string, unsigned int> account = *it;
		strcpy(write_struct.id,account.first.c_str());
		write_struct.item_data = account.second;
		output.write(reinterpret_cast<char*>(&write_struct),sizeof(StoredAccount));
	}
	output.close();
}
void edit_balance(string id, int balance){
	accounts[id] = balance;
	cout << id << ": " << balance << endl;
}
void read_balance(string id){
	if (id=="all"){
		for (map<string, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
			pair<string, unsigned int> account = *it;
			cout << account.first << ": " << flush;
			cout << account.second << endl;
		}
	}else{
		cout << accounts[id] << endl;
	}
}
int main(int argc, const char * argv[]){
	map_data();
	if (*argv[1] == 'r'){
		if (*argv[2] == 'a'){
			read_balance("all");
		}else{
			read_balance(argv[2]);
		}
	}
	if (*argv[1] == 'w'){
		edit_balance(argv[2], stoul(argv[3]));
	}
	write_data();
	return 0;
}
