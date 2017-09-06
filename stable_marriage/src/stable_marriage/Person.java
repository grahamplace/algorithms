package stable_marriage;

public class Person {

	public int id;
	public char gender;
	public String name;
	public int spouse;
	private int[] preferenceList;
	private String inputString;

	// Constructor for input string in format: "3 M Ray 7,6,5,8"
	public Person(String input) {
		inputString = input;

		String[] parts = input.split(" ");

		id = Integer.parseInt(parts[0]);

		gender = parts[1].charAt(0);

		name = parts[2];

		spouse = -1;

		String[] p = parts[3].split(",");
		preferenceList = new int[p.length];
		for (int i = 0; i < p.length; i++) {
			preferenceList[i] = Integer.parseInt(p[i]);
		}
	}

	public int[] getPreferenceList() {
		return preferenceList;
	}

	public String toString() {
		return inputString;
	}
}
