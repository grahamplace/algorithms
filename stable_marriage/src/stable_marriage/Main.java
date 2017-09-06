package stable_marriage;

public class Main {

	public static void main(String[] args) {

		if (args.length == 0) {
			System.out.println("Please run the program with a filename passed in, i.e. 'java myProgram test1.text'");
			return;
		}

		System.out.println("Attempting to run using file " + args[0] + "\n");
		TraditionalMarriage tma = new TraditionalMarriage(args[0]);

	}

}
