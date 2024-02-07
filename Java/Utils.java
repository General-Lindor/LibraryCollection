package de.kalender.utils;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Utils {
	

	public static boolean leapYear (int year) {
		boolean boolOne = (year % 4 == 0);
		boolean boolTwo = (year % 100 == 0);
		boolean boolThree = (year % 400 == 0);
		boolean boolTotal = boolThree | (boolOne & (!boolTwo));
		return boolTotal;
	}

	public static int getDaysOfYear (int year) {
		boolean leap = leapYear(year);
		if (leap) {
			return 366;
		}
		else {
			return 365;
		}
	}

	public static int getDaysOfMonth (int year, int month) {
		if (month == 2) {
			boolean leap = leapYear(year);
			if (leap) {
				return 29;
			}
			else {
				return 28;
			}
		}
		else if (month < 8) {
			if (month % 2 == 0) {
				return 30;
			}
			else {
				return 31;
			}
		}
		else if (month % 2 == 0) {
				return 31;
			}
		else {
			return 30;
		}
	}

	public static String getDay(int year, int month, int day) {
		String[] names = new String[] {"Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"};
		int days = 0;
		boolean bool = false;
		if (year > 2022) {
			days = days + getDaysOfMonth(2022, 10) - 24;
			for (int i = 11; i <= 12; i++) {
				days = days + getDaysOfMonth(2022, i);
			}
			for (int i = 2023; i < year; i++) {
				days = days + getDaysOfYear(i);
			}
			for (int i = 1; i < month; i++) {
				days = days + getDaysOfMonth(year, i);
			}
			days = days + day;
		}
		else if (year < 2022) {
			bool = true;
			days = days + getDaysOfMonth(year, month) - day;
			for (int i = month + 1; i <= 12; i++) {
				days = days + getDaysOfMonth(year, i);
			}
			for (int i = year + 1; i <= 2021; i++) {
				days = days + getDaysOfYear(i);
			}
			for (int i = 1; i <= 9; i++) {
				days = days + getDaysOfMonth(2022, i);
			}
			days = days + 24;
		}
		else {
			if (month > 10) {
				days = days + getDaysOfMonth(2022, 10) - 24;
				for (int i = 11; i < month; i++) {
					days = days + getDaysOfMonth(2022, i);
				}
				days = days + day;
			}
			else if (month < 10) {
				bool = true;
				days = days + getDaysOfMonth(year, month) - day;
				for (int i = month + 1; i <= 9; i++) {
					days = days + getDaysOfMonth(year, i);
				}
				days = days + 24;
			}
			else {
				if (day > 24) {
					days = day - 24;
				}
				else if (day < 24) {
					bool = true;
					days = 24 - day;
				}
				else {
					return names[0];
				}
			}
		}
		days = days % 7;
		if (bool) {
			days = 8 - days;
			if (days == 8) {
				days = 1;
			}
			days = days - 1;
		}
		return names[days];
	}

	public static String getMonth(int month) {
		String[] names = new String[] {"Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"};
		return names[month - 1];
	}

	public static String execute (String s) throws Exception {
		ProcessBuilder builder = new ProcessBuilder("cmd.exe", "/c", s);
		builder.redirectErrorStream(true);
		Process p = builder.start();
		BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
		String line = "";
		while (true) {
			String newline = r.readLine();
			if (newline == null) {
				break;
			}
			else {
				line = line + newline;
			}
		}
		return line;
	}
	
	public static String dateToString (int year, int month, int day) {
		String result = Integer.toString(year) + formatNumber(month) + formatNumber(day);
		return result;
	}
	
	public static int[] intToDate (String number) {
		int[] result = new int[] {Integer.parseInt(number.substring(0, 4)), Integer.parseInt(number.substring(4, 6)), Integer.parseInt(number.substring(6, 8))};
		return result;
	}
		
	public static String formatNumber(int number) {
		if (number < 10) {
			String result = "0" + Integer.toString(number);
			return result;
		}
		else {
			return Integer.toString(number);
		}
	}

}
