package stable_marriage;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class TraditionalMarriage {

	public static void main(String[] args) {
		int n = 0;
		Person[] people = null;
		try {
			File file = new File("test1.txt");
			FileReader fileReader = new FileReader(file);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			String line;
			int lineCount = 0;
			while ((line = bufferedReader.readLine()) != null) {
				if (lineCount == 0) {
					n = Integer.parseInt(line);
					lineCount++;
					continue;
				} else if (lineCount == 1) {
					people = new Person[n];
				}

				if (n > 0 && lineCount <= n / 2) {
					people[lineCount - 1] = new Male(line);
				} else if (n > 0 && lineCount > n / 2) {
					people[lineCount - 1] = new Female(line);
				}
				lineCount++;
			}
			fileReader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
