---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Fourth FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# Fourth FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 1 / Fourth FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1672** Fourth FIToFICustomerCreditTransfer

**P1673** Description

**P1674** On receipt of the message of BBBB Bank, EEEE Bank debits the account of BBBB Bank and credits its customer ZZ Insurances as instructed in the second payment transaction. EEEE Bank creates a new FIToFICustomerCreditTransfer to execute the first payment transaction and sends it to creditor agent DDDDBEBB through the clearing system XYZ of which both banks are members.

**P1675** Business Data 

**P1676** FIToFICustomerCreditTransfer from EEEEDEFF to DDDDBEBB:

[T38 - complete table](../tables/tbl-0038.md)

**P1677** Message Instance

**P1678** <FIToFICstmrCdtTrf>

**P1679** 	<GrpHdr>

**P1680** 		<MsgId>EEEE/150929-EUR/059</MsgId>

**P1681** 		<CreDtTm>2015-09-29T09:00:00</CreDtTm>

**P1682** 		<NbOfTxs>1</NbOfTxs>

**P1683** 		<SttlmInf>

**P1684** 			<SttlmMtd>CLRG</SttlmMtd>

**P1685** 			<ClrSys>

**P1686** 				<Prtry>XYZ</Prtry>

**P1687** 			</ClrSys>

**P1688** 		</SttlmInf>

**P1689** 		<InstgAgt>

**P1690** 			<FinInstnId>

**P1691** 				<BICFI>EEEEDEFF</BICFI>

**P1692** 			</FinInstnId>

**P1693** 		</InstgAgt>

**P1694** 		<InstdAgt>

**P1695** 			<FinInstnId>

**P1696** 				<BICFI>DDDDBEBB</BICFI>

**P1697** 			</FinInstnId>

**P1698** 		</InstdAgt>

**P1699** 	</GrpHdr>

**P1700** 	<CdtTrfTxInf>

**P1701** 		<PmtId>

**P1702** 			<InstrId>EEEE/150929-EUR/059/1</InstrId>

**P1703** 			<EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>

**P1704** 			<TxId>BBBB/150928-CCT/EUR/912/1</TxId>

**P1705** 		</PmtId>

**P1706** 		<PmtTpInf>

**P1707** 			<InstrPrty>NORM</InstrPrty>

**P1708** 		</PmtTpInf>

**P1709** 		<IntrBkSttlmAmt Ccy="EUR">499250</IntrBkSttlmAmt>

**P1710** 		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>

**P1711** 		<InstdAmt Ccy="EUR">500000</InstdAmt>

**P1712** 		<ChrgBr>CRED</ChrgBr>

**P1713** 		<ChrgsInf>

**P1714** 			<Amt Ccy="EUR">500</Amt>

**P1715** 			<Agt>

**P1716** 				<FinInstnId>

**P1717** 					<BICFI>BBBBUS33</BICFI>

**P1718** 				</FinInstnId>

**P1719** 			</Agt>

**P1720** 		</ChrgsInf>

**P1721** 		<ChrgsInf>

**P1722** 			<Amt Ccy="EUR">250</Amt>

**P1723** 			<Agt>

**P1724** 				<FinInstnId>

**P1725** 					<BICFI>EEEEDEFF</BICFI>

**P1726** 				</FinInstnId>

**P1727** 			</Agt>

**P1728** 		</ChrgsInf>

**P1729** 		<Dbtr>

**P1730** 			<Nm>ABC Corporation</Nm>

**P1731** 			<PstlAdr>

**P1732** 				<StrtNm>Times Square</StrtNm>

**P1733** 				<BldgNb>7</BldgNb>

**P1734** 				<PstCd>NY 10036</PstCd>

**P1735** 				<TwnNm>New York</TwnNm>

**P1736** 				<Ctry>US</Ctry>

**P1737** 			</PstlAdr>

**P1738** 		</Dbtr>

**P1739** 		<DbtrAcct>

**P1740** 			<Id>

**P1741** 				<Othr>

**P1742** 						<Id>00125574999</Id>

**P1743** 				</Othr>

**P1744** 			</Id>

**P1745** 		</DbtrAcct>

**P1746** 		<DbtrAgt>

**P1747** 			<FinInstnId>

**P1748** 				<BICFI>BBBBUS33</BICFI>

**P1749** 			</FinInstnId>

**P1750** 		</DbtrAgt>

**P1751** 		<CdtrAgt>

**P1752** 			<FinInstnId>

**P1753** 				<BICFI>DDDDBEBB</BICFI>

**P1754** 			</FinInstnId>

**P1755** 		</CdtrAgt>

**P1756** 		<Cdtr>

**P1757** 			<Nm>GHI Semiconductors</Nm>

**P1758** 			<PstlAdr>

**P1759** 				<StrtNm>Avenue Brugmann</StrtNm>

**P1760** 				<BldgNb>415</BldgNb>

**P1761** 				<PstCd>1180</PstCd>

**P1762** 				<TwnNm>Brussels</TwnNm>

**P1763** 				<Ctry>BE</Ctry>

**P1764** 			</PstlAdr>

**P1765** 		</Cdtr>

**P1766** 		<CdtrAcct>

**P1767** 			<Id>

**P1768** 				<IBAN>BE30001216371411</IBAN>

**P1769** 			</Id>

**P1770** 		</CdtrAcct>

**P1771** 		<Purp>

**P1772** 			<Cd>GDDS</Cd>

**P1773** 		</Purp>

**P1774** 		<RmtInf>

**P1775** 			<Strd>

**P1776** 				<RfrdDocInf>

**P1777** 					<Tp>

**P1778** 						<CdOrPrtry>

**P1779** 							<Cd>CINV</Cd>

**P1780** 						</CdOrPrtry>

**P1781** 					</Tp>

**P1782** 					<Nb>ABC-13679</Nb>

**P1783** 					<RltdDt>

**P1784** 					<Tp>

**P1785** 						<Cd>INDA</Cd>

**P1786** 					</Tp>

**P1787** 					<Dt>2015-09-15</Dt>									

**P1788** 					</RltdDt>					

**P1789** 				</RfrdDocInf>

**P1790** 			</Strd>

**P1791** 		</RmtInf>

**P1792** 	</CdtTrfTxInf>

**P1793** </FIToFICstmrCdtTrf>

