#include <iostream>
#include <stack>
#include <queue>
#include <map>
#include <math.h>
#include <string.h>

using namespace std;

map<char,pair<int,int>> operator_info = {
	{'+',pair<int,int>(1,-1)},
	{'-',pair<int,int>(1,-1)},
	{'*',pair<int,int>(2,-1)},
	{'/',pair<int,int>(2,-1)},
	{'^',pair<int,int>(3,1)}
};

char* operators = new char[5]{'+','-','*','/','^'};

string input;

float evaluate_postfix(queue<string> postfix_queue){
	int operand_counter=0;
	stack<float> postfix_stack;
	pair<float,float> operands;
	bool is_operator;
	while (!postfix_queue.empty()){
		string token = postfix_queue.front();
		postfix_queue.pop();
		is_operator=false;
		for (int i=0;i<5;i++){
			if (operators[i]==token[0]){
				is_operator=true;
			}
		}
		if (is_operator){
			operands.second=postfix_stack.top();
			postfix_stack.pop();
			operands.first=postfix_stack.top();
			postfix_stack.pop();
			switch (token[0]){
				case '+':
					postfix_stack.push(operands.first+operands.second);
					break;
				case '-':
					postfix_stack.push(operands.first-operands.second);
					break;
				case '*':
					postfix_stack.push(operands.first*operands.second);
					break;
				case '/':
					postfix_stack.push(operands.first/operands.second);
					break;
				case '^':
					postfix_stack.push(pow(operands.first,operands.second));
					break;
			}
		}else{
			postfix_stack.push(stof(token));
		}
	}
	return postfix_stack.top();
}

queue<string> tokenize_input(string input){
	queue<string> out_queue;
	for (int i=0;i<input.length();i++){
		string token="";
		if (!isdigit(input[i]) && input[i] != ' '){
			token=input[i];
		}else if (input[i] != ' '){
			while (i<input.length()){
				token+=input[i];
				if (i+1==input.length()){
					break;
				}
				if (input[i+1] == ' ' || input[i+1] != '.' && !isdigit(input[i+1])){
					break;
				}
				i++;
			}
		}
		out_queue.push(token);
	}
	return out_queue;
}

queue<string> parse_input(string input){
	queue<string> token_queue = tokenize_input(input);
	if (token_queue.empty()){
		exit(-1);
	}
	cout << "INFIX: ";
	queue<string> infix_queue=token_queue;
	while (!infix_queue.empty()){
		cout << infix_queue.front() << " ";
		infix_queue.pop();
	}
	cout << endl;
	queue<string> out_queue;
	stack<char> op_stack;
	while (!token_queue.empty()){
		string token=token_queue.front();
		token_queue.pop();
		if (isdigit(token[0])){
			out_queue.push(token);
		}
		if (token[0]=='('){
			op_stack.push(token[0]);
		}
		if (token[0]==')'){
			while (op_stack.top() != '('){
				out_queue.push(string(1,op_stack.top()));
				op_stack.pop();
			}
			op_stack.pop();
		}
		bool is_operator=false;
		for (int i=0;i<5;i++){
			if (operators[i]==token[0]){
				is_operator=true;
				break;
			}
		}
		if (is_operator){
			int precedence=operator_info.at(token[0]).first;
			int direction=operator_info.at(token[0]).second;
			if (!op_stack.empty()){
				int top_precedence;
				if (op_stack.top() == '('){
					top_precedence=0;
				}else{
					top_precedence = operator_info.at(op_stack.top()).first;
				}
				while (!op_stack.empty() && (precedence<top_precedence || (precedence==top_precedence && direction==-1))){
					if (op_stack.top()=='('){
						break;
					}
					out_queue.push(string(1,op_stack.top()));
					op_stack.pop();
					if (!op_stack.empty() && op_stack.top() != '('){
						top_precedence = operator_info.at(op_stack.top()).first;
						direction = operator_info.at(op_stack.top()).second;
					}
				}
			}
			op_stack.push(token[0]);
		}
	}
	while (!op_stack.empty()){
		out_queue.push(string(1,op_stack.top()));
		op_stack.pop();
	}
	cout << "POSTFIX: ";
	queue<string> ret_queue=out_queue;
	while (out_queue.size()>0){
		cout << out_queue.front() << " ";
		out_queue.pop();
	}
	cout << endl;
	return ret_queue;
}

int main(int argc, const char * argv[]){
	if (strlen(argv[1])>0){
		cout << evaluate_postfix(parse_input(argv[1])) << endl;
	}
}
