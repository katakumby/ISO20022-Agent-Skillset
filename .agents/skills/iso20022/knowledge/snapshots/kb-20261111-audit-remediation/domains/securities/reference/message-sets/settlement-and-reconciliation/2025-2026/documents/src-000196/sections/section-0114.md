---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionInstruction sese.023.001.13"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionInstruction sese.023.001.13

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesSettlementTransactionInstruction sese.023.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1730** SecuritiesSettlementTransactionInstruction sese.023.001.13

**P1731** Description

**P1732** On the 12 January 2019, Dresdner Bank Frankfurt (DRESDEFF), the account owner, instructs their sub-custodian Dresdner Bank London (DRESGB2L) to receive against payment securities in favour of their customer JP Morgan Investment GMBH Frankfurt (MGTCDE55).  The securities are to be delivered by Midland Bank PLC London (MIDLGB2L) on behalf of Commerz Financial Products GMBH Frankfurt (CFPIDEFF). This is done through a Securities Settlement Transaction Instruction (sese.023.001.07).

**P1733** Business Data

**P1734** Transaction Identification: FRTJ123REC2

**P1735** Securities Movement Type: receive

**P1736** Payment: against payment

**P1737** Trade Date: 12/01/2019

**P1738** Settlement Date: 15/01/2019

**P1739** Deal Price Value Type: par value

**P1740** Rate: 101.001283

**P1741** Financial Instrument: GB0987654321

**P1742** Quantity: face amount 4,000,000

**P1743** Safekeeping Account: 222S

**P1744** Securities Transaction Type: trade

**P1745** Delivering Depository: CRSTGB22 (CREST)

**P1746** Delivering Party 1: CREST account 456

**P1747** Delivering Party 2: CPFIDEFF (Commerz Financial Products GmbH, Frankfurt

**P1748** Receiving Settlement Party 1: CREST account 123

**P1749** Receiving Settlement Party 2: DRESDEFF (Dresdner Bank Frankfurt)

**P1750** Receiving Settlement Party 3: MGTCDE55 (JP Morgan Investment GmbH,

**P1751** Frankfurt) account 111S

**P1752** Settlement Amount GBP 4,047,151.3 debit

**P1753** Message Instance

**P1754** <SctiesSttlmTxInstr>

**P1755** 	<TxId>FRTJ123REC2</TxId>

**P1756** 	<SttlmTpAndAddtlParams>

**P1757** 		<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1758** 		<Pmt>APMT</Pmt>

**P1759** 	</SttlmTpAndAddtlParams>

**P1760** 	<TradDtls>

**P1761** 		<TradDt>

**P1762** 			<Dt>

**P1763** 				<Dt>2019-01-12</Dt>

**P1764** 			</Dt>

**P1765** 		</TradDt>

**P1766** 		<SttlmDt>

**P1767** 			<Dt>

**P1768** 				<Dt>2019-01-15</Dt>

**P1769** 			</Dt>

**P1770** 		</SttlmDt>

**P1771** 		<DealPric>

**P1772** 			<Tp>

**P1773** 				<ValTp>PARV</ValTp>

**P1774** 			</Tp>

**P1775** 			<Val>

**P1776** 				<Rate>101.001283</Rate>

**P1777** 			</Val>

**P1778** 		</DealPric>

**P1779** 	</TradDtls>

**P1780** 	<FinInstrmId>

**P1781** 		<ISIN>GB0987654321</ISIN>

**P1782** 	</FinInstrmId>

**P1783** 	<QtyAndAcctDtls>

**P1784** 		<SttlmQty>

**P1785** 			<Qty>

**P1786** 				<FaceAmt>4000000</FaceAmt>

**P1787** 			</Qty>

**P1788** 		</SttlmQty>

**P1789** 		<SfkpgAcct>

**P1790** 			<Id>222S</Id>

**P1791** 		</SfkpgAcct>

**P1792** 	</QtyAndAcctDtls>

**P1793** 	<SttlmParams>

**P1794** 		<SctiesTxTp>

**P1795** 			<Cd>TRAD</Cd>

**P1796** 		</SctiesTxTp>

**P1797** 	</SttlmParams>

**P1798** 	<DlvrgSttlmPties>

**P1799** 		<Dpstry>

**P1800** 			<Id>

**P1801** 				<AnyBIC>CRSTGB22</AnyBIC>

**P1802** 			</Id>

**P1803** 		</Dpstry>

**P1804** 		<Pty1>

**P1805** 			<Id>

**P1806** 				<PrtryId>

**P1807** 					<Id>456</Id>

**P1808** 					<Issr>CRST</Issr>

**P1809** 				</PrtryId>

**P1810** 			</Id>

**P1811** 		</Pty1>

**P1812** 		<Pty2>

**P1813** 			<Id>

**P1814** 				<AnyBIC>CPFIDEFF</AnyBIC>

**P1815** 			</Id>

**P1816** 		</Pty2>

**P1817** 	</DlvrgSttlmPties>

**P1818** 	<RcvgSttlmPties>

**P1819** 		<Pty1>

**P1820** 			<Id>

**P1821** 				<PrtryId>

**P1822** 					<Id>123</Id>

**P1823** 					<Issr>CRST</Issr>

**P1824** 				</PrtryId>

**P1825** 			</Id>

**P1826** 		</Pty1>

**P1827** 		<Pty2>

**P1828** 			<Id>

**P1829** 				<AnyBIC>DRESDEFF</AnyBIC>

**P1830** 			</Id>

**P1831** 		</Pty2>

**P1832** 		<Pty3>

**P1833** 			<Id>

**P1834** 				<AnyBIC>MGTCDE55</AnyBIC>

**P1835** 			</Id>

**P1836** 			<SfkpgAcct>

**P1837** 				<Id>111S</Id>

**P1838** 			</SfkpgAcct>

**P1839** 		</Pty3>

**P1840** 	</RcvgSttlmPties>

**P1841** 	<SttlmAmt>

**P1842** 		<AcrdIntrstInd>true</AcrdIntrstInd>

**P1843** 		<Amt Ccy="GBP">4047151.3</Amt>

**P1844** 		<CdtDbtInd>DBIT</CdtDbtInd>

**P1845** 	</SttlmAmt>

**P1846** </SctiesSttlmTxInstr>

