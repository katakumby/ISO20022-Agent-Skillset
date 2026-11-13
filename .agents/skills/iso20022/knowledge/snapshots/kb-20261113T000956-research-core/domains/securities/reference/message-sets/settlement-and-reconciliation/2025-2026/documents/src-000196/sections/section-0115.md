---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionStatusAdvice sese.024.001.14"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionStatusAdvice sese.024.001.14

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesSettlementTransactionStatusAdvice sese.024.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1847** SecuritiesSettlementTransactionStatusAdvice sese.024.001.14

**P1848** Description

**P1849** On the 7 January 2019, Dresdner Bank London (DRESGB2L) advises its customer Dresdner Bank Frankfurt (DRESDEFF) on the status of the previously sent Receive Against Payment instruction.

**P1850** Business Data

**P1851** Account Owner transaction Id: FRTJ123REC2

**P1852** Matching status (no reason): matched

**P1853** Transaction Details: Safekeeping Account 222S

**P1854** Financial Instrument: GB0987654321

**P1855** Quantity: face amount 4,000,000

**P1856** Settlement Amount: GBP 4,047,151.3 debit

**P1857** Trade date: 05/01/2019

**P1858** Settlement Date: 08/01/2019

**P1859** Securities Movement Type: receive

**P1860** Payment: against payment

**P1861** Securities Transaction Type: trade

**P1862** Delivering Depository: CRSTGB22 (CREST)

**P1863** Delivering Party 1: CREST account 456

**P1864** Delivering Party 2: CPFIDEFF (Commerz Financial Products GmbH, Frankfurt)

**P1865** Message Instance

**P1866** <SctiesSttlmTxStsAdvc>

**P1867** 	<TxId>

**P1868** 		<AcctOwnrTxId>FRTJ123REC2</AcctOwnrTxId>

**P1869** 	</TxId>

**P1870** 	<MtchgSts>

**P1871** 		<Mtchd>

**P1872** 			<Rsn>

**P1873** 			<Id>ABCD</Id>

**P1874** 			<Issr>SGX</Issr>

**P1875** 			</Rsn>

**P1876** 		</Mtchd>

**P1877** 	</MtchgSts>

**P1878** 	<TxDtls>

**P1879** 		<SfkpgAcct>

**P1880** 			<Id>222S</Id>

**P1881** 		</SfkpgAcct>

**P1882** 		<FinInstrmId>

**P1883** 			<ISIN>GB0987654321</ISIN>

**P1884** 			</FinInstrmId>

**P1885** 		<SttlmQty>

**P1886** 			<Qty>

**P1887** 				<FaceAmt>4000000</FaceAmt>

**P1888** 			</Qty>

**P1889** 		</SttlmQty>

**P1890** 		<SttlmAmt>

**P1891** 			<Amt Ccy="GBP">4047151.3</Amt>

**P1892** 			<CdtDbtInd>DBIT</CdtDbtInd>

**P1893** 		</SttlmAmt>

**P1894** 		<SttlmDt>

**P1895** 			<Dt>

**P1896** 				<Dt>2019-01-08</Dt>

**P1897** 			</Dt>

**P1898** 		</SttlmDt>

**P1899** 		<TradDt>

**P1900** 			<Dt>

**P1901** 				<Dt>2019-01-05</Dt>

**P1902** 			</Dt>

**P1903** 		</TradDt>

**P1904** 		<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1905** 		<Pmt>APMT</Pmt>

**P1906** 		<SttlmParams>

**P1907** 			<SctiesTxTp>

**P1908** 				<Cd>TRAD</Cd>

**P1909** 			</SctiesTxTp>

**P1910** 		</SttlmParams>

**P1911** 		<RcvgSttlmPties>

**P1912** 			<Dpstry>

**P1913** 				<Id>

**P1914** 					<AnyBIC>CRSTGB22</AnyBIC>

**P1915** 				</Id>

**P1916** 			</Dpstry>

**P1917** 			<Pty1>

**P1918** 				<Id>

**P1919** 					<PrtryId>

**P1920** 						<Id>456</Id>

**P1921** 						<Issr>CRST</Issr>

**P1922** 					</PrtryId>

**P1923** 				</Id>

**P1924** 			</Pty1>

**P1925** 			<Pty2>

**P1926** 				<Id>

**P1927** 					<AnyBIC>CPFIDEFF</AnyBIC>

**P1928** 				</Id>

**P1929** 			</Pty2>

**P1930** 		</RcvgSttlmPties>

**P1931** 	</TxDtls>

**P1932** </SctiesSttlmTxStsAdvc>

