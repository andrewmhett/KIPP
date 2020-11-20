#include <iostream>
#include <fstream>
#include <map>
#include <vector>

using namespace std;

map<long long, unsigned int> accounts;

#pragma pack(push, 1)
struct Account{
	long long id;
	unsigned int balance;
};
#pragma pack(pop)

void map_data(){
	ifstream input;
	input.open("$KIPP_DIR/C++/KIPPCOINS.bin", ios::binary);		
	vector<Account> accounts_v;
	char char_buf;
	while (input >> char_buf){
		input.putback(char_buf);
		Account read_struct;
		input.read(reinterpret_cast<char*>(&read_struct),sizeof(Account));
		accounts_v.push_back(read_struct);
	}
	input.close();
	for(vector<Account>::iterator it = accounts_v.begin(); it != accounts_v.end(); ++it){
		Account account = *it;
		accounts[account.id] = account.balance;
	}
}
void write_data(){
	ofstream output;
	output.open("$KIPP_DIR/C++/KIPPCOINS.bin", ios::binary);
	for (map<long long, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
		Account write_struct;
		pair<long long, unsigned int> account = *it;
		write_struct.id=account.first;
		write_struct.balance = account.second;
		output.write(reinterpret_cast<char*>(&write_struct),sizeof(Account));
	}
	output.close();
}
void edit_balance(long long id, int balance){
	accounts[id] = balance;
	cout << id << ": " << balance << endl;
}
void read_balance(long long id){
	if (id==0){
		for (map<long long, unsigned int>::iterator it = accounts.begin(); it != accounts.end(); ++it){
			pair<long long, unsigned int> account = *it;
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
			read_balance(0);
		}else{
			read_balance(atoll(argv[2]));
		}
	}
	if (*argv[1] == 'w'){
		edit_balance(atoll(argv[2]), stoul(argv[3]));
	}
	write_data();
	return 0;
}
