---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Security Report - reda.012.001.01"]
content_origin: "source-transcription"
---

# Security Report - reda.012.001.01

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Security Report - reda.012.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P774** Security Report - reda.012.001.01

**P775** Description

**P776** The Security Report message can be used as answer for:

**P777** Securities Reference Data Query; 

**P778** ISIN List Query;

**P779** Securities CSD Link Query; 

**P780** Securities Deviating Nominal Query;

**P781** performed using the Security Query. This example shows the answer to the Securities Reference Data Query described in the chapter 7.7. The query returns only one security:

**P782** Security Identification: SECXXXYYYZZ1

**P783** Security Long Name: Sample equity shares, Fixed Interest Rate

**P784** Security Short Name: Sample ES, FIR

**P785** Valid From Name: 2020-01-01

**P786** Denomination Currency: EUR

**P787** Expiry Date: 2030-12-31

**P788** Classification Type: ESFTFR

**P789** Country of Issue: IT

**P790** Issue Date: 2020-01-01

**P791** ISIN Valid From: 2020-01-01

**P792** Quantity Type: UNIT

**P793** Minimum Denomination: 100

**P794** Minimum Multiple Quantity: 10

**P795** Deviating Settlement Unit: 13

**P796** Message Instance

**P797** <Document>

**P798** 	<SctyRpt>

**P799** 		<MsgHdr>

**P800** 			<MsgId>NONREF</MsgId>

**P801** 			<OrgnlBizInstr>

**P802** 				<MsgId>SAMPLEQRYSEC001</MsgId>

**P803** 			</OrgnlBizInstr>

**P804** 		</MsgHdr>

**P805** 		<Pgntn>

**P806** 			<PgNb>1</PgNb>

**P807** 			<LastPgInd>true</LastPgInd>

**P808** 		</Pgntn>

**P809** 		<SctyRptOrErr>

**P810** 			<SctyRptOrBizErr>

**P811** 				<SctyRpt>

**P812** 					<FinInstrmId>

**P813** 						<ISIN>SECXXXYYYZZ1</ISIN>

**P814** 					</FinInstrmId>

**P815** 					<FinInstrmAttrbts>

**P816** 						<FinInstrmNm>

**P817** 							<ISOShrtNm>Sample ES, FIR</ISOShrtNm>

**P818** 							<ISOLngNm>Sample equity shares, Fixed Interest Rate</ISOLngNm>

**P819** 							<VldFr>

**P820** 								<Dt>2020-01-01</Dt>

**P821** 							</VldFr>

**P822** 						</FinInstrmNm>

**P823** 						<DnmtnCcy>EUR</DnmtnCcy>

**P824** 						<XpryDt>2030-12-31</XpryDt>

**P825** 						<ClssfctnTp>

**P826** 						<ClssfctnFinInstrm>ESFTFR</ClssfctnFinInstrm>

**P827** 						</ClssfctnTp>

**P828** 						<Issnc>

**P829** 							<CtryOfIsse>IT</CtryOfIsse>

**P830** 							<IsseDt>2020-01-01</IsseDt>

**P831** 						</Issnc>

**P832** 						<FinInstrmIdVldty>

**P833** 							<FinInstrmId>

**P834** 								<ISIN>SECXXXYYYZZ1</ISIN>

**P835** 							</FinInstrmId>

**P836** 							<ISINVldFr>2020-01-01</ISINVldFr>

**P837** 						</FinInstrmIdVldty>

**P838** 						<SttlmInf>

**P839** 							<SctiesQtyTp>

**P840** 								<Cd>UNIT</Cd>

**P841** 							</SctiesQtyTp>

**P842** 							<MinDnmtn>

**P843** 								<Unit>100</Unit>

**P844** 							</MinDnmtn>

**P845** 							<MinMltplQty>

**P846** 								<Unit>10</Unit>

**P847** 							</MinMltplQty>

**P848** 							<DevtgSttlmUnit>

**P849** 								<Unit>13</Unit>

**P850** 							</DevtgSttlmUnit>

**P851** 						</SttlmInf>

**P852** 					</FinInstrmAttrbts>

**P853** 				</SctyRpt>

**P854** 			</SctyRptOrBizErr>

**P855** 		</SctyRptOrErr>

**P856** 	</SctyRpt>

**P857** </Document>

