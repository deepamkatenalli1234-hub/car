class Car:
    def __init__(self, cid, brand, model, year, scores):
        self.cid, self.brand, self.model, self.year, self.scores = cid, brand, model, year, scores

    def avg(self): return sum(self.scores)/len(self.scores)
    def cat(self):
        a=self.avg()
        return "Luxury" if a>=90 else "High Performance" if a>=80 else "Standard" if a>=65 else "Basic" if a>=50 else "Below Average" if a>=40 else "Poor"

    def save(self, file="car_report.txt"):
        with open(file,"w") as f:
            f.write(f"Car {self.cid} - {self.brand} {self.model} ({self.year})\nScores: {self.scores}\nAverage: {self.avg():.2f}\nCategory: {self.cat()}")
        print(f"Report saved to {file}")

def main():
    car=Car(input("ID: "),input("Brand: "),input("Model: "),input("Year: "),[int(input(f"Score {i}: ")) for i in range(1,4)])
    car.save()

if __name__=="__main__": main()