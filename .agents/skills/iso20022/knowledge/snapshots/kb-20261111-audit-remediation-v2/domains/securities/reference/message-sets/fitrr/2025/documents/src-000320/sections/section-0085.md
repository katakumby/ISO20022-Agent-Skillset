---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Transaction Reporting", "auth.016.001.03 "]
content_origin: "source-transcription"
---

# auth.016.001.03 

Source: [src-000320](../../../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Locator: heading path Business Examples / Transaction Reporting / auth.016.001.03 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P780** auth.016.001.03 

**P781** Description

**P782** The following MessageInstance provides an example of a Transaction Report Message that is being executed and reported by the entity with LEI 00000000000000000000. The transaction was executed in the instrument identified by AB1234567890 and took place on the venue XDUB.

**P783** Message Instance

**P784** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.016.001.03">

**P785** 	<FinInstrmRptgTxRpt>

**P786** 		<Tx>

**P787** 			<New>

**P788** 				<TxId>T123456</TxId>

**P789** 				<ExctgPty>00000000000000000000</ExctgPty>

**P790** 				<InvstmtPtyInd>true</InvstmtPtyInd>

**P791** 				<SubmitgPty>00000000000000000000</SubmitgPty>

**P792** 				<Buyr>

**P793** 					<AcctOwnr>

**P794** 						<Id>

**P795** 							<LEI>11111111111111111111</LEI>

**P796** 						</Id>

**P797** 					</AcctOwnr>

**P798** 				</Buyr>

**P799** 				<Sellr>

**P800** 					<AcctOwnr>

**P801** 						<Id>

**P802** 							<LEI>22222222222222222222</LEI>

**P803** 						</Id>

**P804** 					</AcctOwnr>

**P805** 				</Sellr>

**P806** 				<OrdrTrnsmssn>

**P807** 					<TrnsmssnInd>true</TrnsmssnInd>

**P808** 				</OrdrTrnsmssn>

**P809** 				<Tx>

**P810** 					<TradDt>2018-12-17T09:30:47Z</TradDt>

**P811** 					<TradgCpcty>MTCH</TradgCpcty>

**P812** 					<Qty>

**P813** 						<Unit>100</Unit>

**P814** 					</Qty>

**P815** 					<Pric>

**P816** 						<Pric>

**P817** 							<MntryVal>

**P818** 								<Amt Ccy="EUR">13.5</Amt>

**P819** 							</MntryVal>

**P820** 						</Pric>

**P821** 					</Pric>

**P822** 					<TradVn>XDUB</TradVn>

**P823** 				</Tx>

**P824** 				<FinInstrm>

**P825** 					<Id>AB1234567890</Id>

**P826** 				</FinInstrm>

**P827** 				<ExctgPrsn>

**P828** 					<Algo>A123456</Algo>

**P829** 				</ExctgPrsn>

**P830** 				<AddtlAttrbts>

**P831** 					<SctiesFincgTxInd>true</SctiesFincgTxInd>

**P832** 				</AddtlAttrbts>

**P833** 			</New>

**P834** 		</Tx>

**P835** 	</FinInstrmRptgTxRpt>

**P836** </Document>

