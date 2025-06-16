class FileStats:
   
    
    def __init__(self, filename):
       
        self.filename = filename
        self.values = []
        
    def read_file(self):
        
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    try:
                        num = float(line.strip())
                        self.values.append(num)
                    except ValueError:
                        continue
                        
            if not self.values:
                raise ValueError("No valid numbers found in file")
            return True
            
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except ValueError as e:
            print(f"Error: {str(e)}")
            return False
            
    def calculate_stats(self):
        
        if not self.values:
            return None
            
        stats = {
            'sum': sum(self.values),
            'average': sum(self.values) / len(self.values),
            'minimum': min(self.values),
            'maximum': max(self.values)
        }
        return stats
        
    def print_stats(self, stats):
        
        if stats:
            print(f"summation = {stats['sum']}")
            print(f"average = {stats['average']}")
            print(f"minimum = {stats['minimum']}")
            print(f"maximum = {stats['maximum']}")
            
    def process(self):
        if self.read_file():
            stats = self.calculate_stats()
            self.print_stats(stats)

def main():
    filename = input("Enter the filename: ")
    processor = FileStats(filename)
    processor.process()

if __name__ == "__main__":
    main() 