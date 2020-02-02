#include <bits/stdc++.h>
using namespace std;

struct cell{
	vector<int> states;
	int g;
	int next_cell;
	int h;
};

struct compare{
	bool operator()(cell c1, cell c2){
		return c1.g < c2.g;
	}
};

bool isSafe(vector<int> now, int row, int col){
	for(int i=0; i<now.size(); i++){
		if(now[i] == row || abs(now[i]-row) == abs(col-i)){
			return false;
		}
	}
	return true;
}

cell make_new_cell(cell val, int next_row, int n){
	vector<int> v;
	if(val.states.size()){
		v.assign(val.states.begin(), val.states.end());
	}
	v.push_back(next_row);
	cell new_cell;
	new_cell.states = v;
	new_cell.g = val.g + val.h + 1;
	new_cell.next_cell = v.size();
	val.h = n - val.states.size();
	return new_cell;
}

bool isGoalState(vector<int> v){
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<v.size(); j++){
			if(i==j) continue;
			if(v[i] == v[j] || abs(v[i]-v[j]) == abs(i-j)){
				return false;
			}
		}
	}
	return true;
}

void printGoalState(vector<int> v){
	cout << "[ ";
	for(auto i : v){
		cout << i << " ";
	}
	cout << "]\n";
}

int total_ans = 0;

void astar(priority_queue<cell, vector<cell>, compare> q, int n){
	int next_first_cell = 1;
	while(true){
		cell val;
		if(q.size()){
			val = q.top();
			q.pop();
		}
		else{
			if(next_first_cell == n) return;
			val.states.push_back(next_first_cell++);
			val.g = 1;
			val.next_cell = 1;
			val.h = n - 0;
		}
		if(val.states.size() == n){
			if(isGoalState(val.states)){
				total_ans++;
				printGoalState(val.states);
			}
			continue;
		}
		for(int i=0; i<n; i++){
			if(isSafe(val.states, i, val.next_cell)){
				cell new_cell = make_new_cell(val, i, n);
				q.push(new_cell);
			}
		}
	}
}

int main(){
	int n;
	cout<<"n = ";
	cin>>n;

	priority_queue<cell, vector<cell>, compare> q;
	cell first;
	first.states.push_back(0);
	first.g = 1;
	first.next_cell = 1;
	first.h = n - 0;
	q.push(first);

	astar(q,n);

	cout << "total answers = " << total_ans<<endl;
}
