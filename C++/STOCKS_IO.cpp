#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <cstring>

using namespace std;

map<string, int[2]> accounts;

#pragma pack(push, 1)
struct Account {
								string id;
								int stock_data[2];
};
struct StoredAccount {
								char id[5];
								int num_shares;
								int price_per_share;
};
#pragma pack(pop)

void map_data(){
								ifstream input;
								string KIPP_PATH;
								KIPP_PATH=getenv("KIPP_DIR");
								input.open(KIPP_PATH+"/C++/STOCKS.bin", ios::binary);
								vector<Account> accounts_v;
								char char_buf;
								while (input >> char_buf) {
																input.putback(char_buf);
																StoredAccount read_struct;
																input.read(reinterpret_cast<char*>(&read_struct),sizeof(StoredAccount));
																Account new_struct;
																string id_str(read_struct.id);
																new_struct.id=id_str;
																new_struct.stock_data[0]=read_struct.num_shares;
																new_struct.stock_data[1]=read_struct.price_per_share;
																accounts_v.push_back(new_struct);
								}
								input.close();
								for(vector<Account>::iterator it = accounts_v.begin(); it != accounts_v.end(); ++it) {
																Account account = *it;
																accounts[account.id][0]=account.stock_data[0];
																accounts[account.id][1]=account.stock_data[1];
								}
}
void write_data(){
								string KIPP_PATH;
								KIPP_PATH=getenv("KIPP_DIR");
								ofstream output;
								output.open(KIPP_PATH+"/C++/STOCKS.bin", ios::binary);
								for (map<string, int[2]>::iterator it = accounts.begin(); it != accounts.end(); ++it) {
																StoredAccount write_struct;
																pair<string, int[2]> account;
																account.first=it->first;
																account.second[0]=it->second[0];
																account.second[1]=it->second[1];
																strcpy(write_struct.id,account.first.c_str());
																write_struct.num_shares = account.second[0];
																write_struct.price_per_share = account.second[1];
																output.write(reinterpret_cast<char*>(&write_struct),sizeof(StoredAccount));
								}
								output.close();
}
void edit_price_per_share(string id, int price_per_share){
								accounts[id][1] = price_per_share;
								cout << id << " (price per share): " << price_per_share << endl;
}
void edit_num_shares(string id, int num_shares){
								accounts[id][0] = num_shares;
								cout << num_shares << endl;
								cout << id << " (number of shares): " << num_shares << endl;
}
void read_data(string id){
								if (id=="all") {
																for (map<string, int[2]>::iterator it = accounts.begin(); it != accounts.end(); ++it) {
																								pair<string, int[2]> account;
																								account.first = it->first;
																								account.second[0]=it->second[0];
																								account.second[1]=it->second[1];
																								cout << account.first << ": " << flush;
																								cout << account.second[0] << " " << account.second[1] << endl;
																}
								}else{
																cout << accounts[id][0] << " " << accounts[id][1] << endl;
								}
}
int main(int argc, const char * argv[]){
								map_data();
								if (*argv[1] == 'r') {
																if (*argv[2] == 'a') {
																								read_data("all");
																}else{
																								read_data(argv[2]);
																}
								}
								if (strcmp(argv[1],"wn")==0) {
																edit_num_shares(argv[2], stoi(argv[3]));
								}
								if (strcmp(argv[1],"wp")==0) {
																edit_price_per_share(argv[2],stoi(argv[3]));
								}
								write_data();
								return 0;
}
