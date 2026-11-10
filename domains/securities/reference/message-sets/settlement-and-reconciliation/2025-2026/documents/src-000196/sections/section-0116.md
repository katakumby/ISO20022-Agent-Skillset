---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionConfirmation sese.025.001.13"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionConfirmation sese.025.001.13

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementTransactionConfirmation sese.025.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1933** SecuritiesSettlementTransactionConfirmation sese.025.001.13

**P1934** Description

**P1935** On the 15 January 2019, Dresdner Bank London (DRESGB2L) confirms the previously instructed movement of securities to its customer, Dresdner Bank Frankfurt (DRESDEFF). The instruction to Receive Against Payment settled on the 15 January 2019. This is done through a Securities Settlement Transaction Confirmation (sese.025.001.07).

**P1936** Business Data

**P1937** Transaction Identification: FRTJ123REC2

**P1938** Securities Movement Type: receive

**P1939** Payment: against payment

**P1940** Trade Date: 12/01/2019

**P1941** Effective Settlement

**P1942** Date: 15/01/2019

**P1943** Deal Price Value Type: par value 

**P1944** Rate: 101.001283

**P1945** Financial Instrument: GB0987654321

**P1946** Quantity: face amount 4,000,000

**P1947** Safekeeping Account: 222S

**P1948** Securities Transaction Type: trade

**P1949** Delivering Depository: CRSTGB22 (CREST

**P1950** Delivering Party 1: CREST account 456 

**P1951** Delivering Party 2: CPFIDEFF (Commerz Financial Products GmbH, Frankfurt)

**P1952** Receiving Depository: NBBEBEBB (National Bank of Belgium

**P1953** Receiving Settlement Party 1: CITIBEBB (Citibank)

**P1954** Receiving Settlement Party 2: CFPIDEFF (Commerz Financial Products GmbH, Frankfurt) account 321654

**P1955** Settlement Amount GBP 4,047,151.3 debit

**P1956** Message Instance

**P1957** <SctiesSttlmTxConf>

**P1958** 	<TxIdDtls>

**P1959** 		<AcctOwnrTxId>FRTJ123REC2</AcctOwnrTxId>

**P1960** 		<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1961** 		<Pmt>APMT</Pmt>

**P1962** 	</TxIdDtls>

**P1963** 	<TradDtls>

**P1964** 		<TradDt>

**P1965** 			<Dt>

**P1966** 				<Dt>2019-01-12</Dt>

**P1967** 			</Dt>

**P1968** 		</TradDt>

**P1969** 		<SttlmDt>

**P1970** 			<Dt>

**P1971** 				<Dt>2019-01-15</Dt>

**P1972** 			</Dt>

**P1973** 		</SttlmDt>

**P1974** 		<FctvSttlmDt>

**P1975** 			<Dt>

**P1976** 				<Dt>2019-01-15</Dt>

**P1977** 			</Dt>

**P1978** 		</FctvSttlmDt>

**P1979** 	</TradDtls>

**P1980** 	<FinInstrmId>

**P1981** 		<ISIN>GB0987654321</ISIN>

**P1982** 	</FinInstrmId>

**P1983** 	<QtyAndAcctDtls>

**P1984** 		<SttldQty>

**P1985** 			<Qty>

**P1986** 				<FaceAmt>4000000</FaceAmt>

**P1987** 			</Qty>

**P1988** 		</SttldQty>

**P1989** 		<SfkpgAcct>

**P1990** 			<Id>222S</Id>

**P1991** 		</SfkpgAcct>

**P1992** 	</QtyAndAcctDtls>

**P1993** 	<SttlmParams>

**P1994** 		<SctiesTxTp>

**P1995** 			<Cd>TRAD</Cd>

**P1996** 		</SctiesTxTp>

**P1997** 	</SttlmParams>

**P1998** 	<DlvrgSttlmPties>

**P1999** 		<Dpstry>

**P2000** 			<Id>

**P2001** 				<AnyBIC>CRSTGB22</AnyBIC>

**P2002** 			</Id>

**P2003** 		</Dpstry>

**P2004** 		<Pty1>

**P2005** 			<Id>

**P2006** 				<PrtryId>

**P2007** 					<Id>456</Id>

**P2008** 					<Issr>CRST</Issr>

**P2009** 				</PrtryId>

**P2010** 			</Id>

**P2011** 		</Pty1>

**P2012** 		<Pty2>

**P2013** 			<Id>

**P2014** 				<AnyBIC>CPFIDEFF</AnyBIC>

**P2015** 			</Id>

**P2016** 		</Pty2>

**P2017** 	</DlvrgSttlmPties>

**P2018** 	<RcvgSttlmPties>

**P2019** 		<Dpstry>

**P2020** 			<Id>

**P2021** 				<AnyBIC>NBBEBEBB</AnyBIC>

**P2022** 			</Id>

**P2023** 		</Dpstry>

**P2024** 		<Pty1>

**P2025** 			<Id>

**P2026** 				<AnyBIC>CITIBEBB</AnyBIC>

**P2027** 			</Id>

**P2028** 		</Pty1>

**P2029** 		<Pty2>

**P2030** 			<Id>

**P2031** 				<AnyBIC>CFPIDEFF</AnyBIC>

**P2032** 			</Id>

**P2033** 			<SfkpgAcct>

**P2034** 				<Id>321654</Id>

**P2035** 			</SfkpgAcct>

**P2036** 		</Pty2>

**P2037** 	</RcvgSttlmPties>

**P2038** 	<SttldAmt>

**P2039** 		<AcrdIntrstInd>true</AcrdIntrstInd>

**P2040** 		<Amt Ccy="GBP">4047151.3</Amt>

**P2041** 		<CdtDbtInd>DBIT</CdtDbtInd>

**P2042** 	</SttldAmt>

**P2043** </SctiesSttlmTxConf>

