package de.kalender.utils;

import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;

public class LayoutHandler {
	
	private ArrayList<ArrayList<Object[]>> JObjects;
	
	public LayoutHandler() {
		resetJObjects();
	}
	
	public void resetJObjects () {
		this.JObjects = new ArrayList<ArrayList<Object[]>>();
	}
		
	public void addJObject (Object O, int X, int Y, boolean newRow) {
		Object[] OA = new Object[] {O, X, Y};
		if (newRow) {
			ArrayList RowList = new ArrayList<Object[]>();
			RowList.add(OA);
			JObjects.add(RowList);
		}
		else {
			ArrayList<Object[]> RowList = JObjects.get(JObjects.size() - 1);
			//for (Object[] OOO : RowList) {
			//}
			RowList.add(OA);
			//for (Object[] OOO : RowList) {
			//}
			JObjects.set(JObjects.size() - 1, RowList);
		}
	}
	
	//dimensions of the whole pane with border
	public int dimx;
	public int dimy;
	//border around whole layout
	public int border = 20;
	//border around each individual object
	public int borderObject = 8;
		
	public JPanel handleJObjects () {
		dimx = 0;
		dimy = 0;
		JPanel Pane = new JPanel();
		int pxTop = border + borderObject;
		int pxBot = 0;
		for (ArrayList<Object[]> Row : JObjects) {
			pxTop += pxBot;
			pxBot = borderObject;
			int pxLeft = border + borderObject;
			for (Object[] O : Row) {
				int xSize = (int)O[1];
				int ySize = (int)O[2];
				try {
					JLabel L = (JLabel)(O[0]);
					L.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(L);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JComboBox C = (JComboBox)(O[0]);
					C.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(C);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JButton B = (JButton)(O[0]);
					B.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(B);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JPasswordField PW = (JPasswordField)(O[0]);
					PW.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(PW);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JTextField TX = (JTextField)(O[0]);
					TX.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(TX);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JTable T = (JTable)(O[0]);
					ySize *= ((DefaultTableModel)(T.getModel())).getRowCount();
					T.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(T);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
				try {
					JScrollPane S = (JScrollPane)(O[0]);
					S.setBounds(pxLeft, pxTop, xSize, ySize);
					Pane.add(S);
					pxLeft += xSize + borderObject;
					int pxBotPot = ySize + borderObject;
					if (pxBotPot > pxBot) {
						pxBot = pxBotPot;
					}
					continue;
				}
				catch (Exception e) {
				}
			}
			if (pxLeft > dimx) {
				dimx = pxLeft;
			}
		}
		dimy = pxTop + pxBot;
		dimx += 2 * border;
		dimy += 2 * border + 20;
		Pane.setBorder(new EmptyBorder(5, 5, 5, 5));
		Pane.setLayout(null);
		return Pane;
	}

	//DEPRECATED! Method to add/subtract px xy size	to object was needed if object changes size, e.g. new row is added to table. Nowadays rows are directly counted and input into dimx and dimy.
	//RowIndex and ColumnIndex does not mean row and column of table! The JObject can be any object, not just tables! Instead, this layout is based on a grid layout with rows and columns, in that sense the LayoutHandler itself is a table, and RowIndex / ColumnIndex are the coords of the object in the layout!
	public void setSize(int RowIndex, int ColumnIndex, int X, int Y, boolean ADD) {
		ArrayList<Object[]> Row = JObjects.get(RowIndex);
		Object[] O = Row.get(ColumnIndex);
		if (ADD) {
			O[1] = (int)O[1] + X;
			O[2] = (int)O[2] + Y;
		}
		else {
			O[1] = X;
			O[2] = Y;
		}
		Row.set(ColumnIndex, O);
		JObjects.set(RowIndex, Row);
	}
}
