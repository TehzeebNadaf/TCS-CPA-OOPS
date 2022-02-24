class Employee:
    def __init__(self, empno: int, empname: str, leaves: dict):
        self.empno = empno
        self.empname = empname
        self.leaves = leaves
class Company(Employee):
    def display_leave(self, req_empno, req_leavetype):
        param = {}
        for i in leaves.keys():
            if i==req_empno:
                param = leaves[i]
            for x in param.keys():
                if x==req_leavetype:
                    return param[req_leavetype]
    def leave_appli(self, req_empno, req_leavetype, req_leaveno):
        self.req_leaveno = req_leaveno
        if req_leaveno==leaves[req_empno][req_leavetype] or req_leaveno<leaves[req_empno][req_leavetype]:
            return "Granted"
        else:
            return "Rejected"

emps = []
leaves = {}
n = int(input())
for i in range(n):
    empno = int(input())
    empname = input()
    leaves[empno] = {}
    leaves[empno]['EL'] = int(input())
    leaves[empno]['SL'] = int(input())
    leaves[empno]['CL'] = int(input())
req_empno = int(input())
req_leavetype = input()
req_leaveno = int(input())

a = Company(empno, empname, leaves).display_leave(req_empno, req_leavetype)
print(a)

b = Company(empno, empname, leaves).leave_appli(req_empno, req_leavetype, req_leaveno)
print(b)      
