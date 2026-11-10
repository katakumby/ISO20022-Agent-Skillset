---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Business Examples", "Party Audit Trail Report - reda.043.001"]
content_origin: "source-transcription"
---

# Party Audit Trail Report - reda.043.001

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Business Examples / Party Audit Trail Report - reda.043.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P688** Party Audit Trail Report - reda.043.001

**P689** Description

**P690** The PartyAuditTrailReport (reda.043) message represents the answer to the Party Audit Trail Query described in the chapter 7.8. In this case, the party with ID PAYBXXYYAAA and responsible party ID NCBAXXYYAAA had only one change performed by the user USER1 and approved by the user USER2 on 2017-08-17T17:59:00 regarding the change of the Postal Code from the value 54321 to the new value 12345. 

**P691** Message Instance

**P692** <Document>

**P693** 	<PtyAudtTrlRpt>

**P694** 		<MsgHdr>

**P695** 			<MsgId>NONREF</MsgId>

**P696** 			<OrgnlBizInstr>

**P697** 				<MsgId>SAMPLEPTYATRQUE</MsgId>

**P698** 			</OrgnlBizInstr>

**P699** 		</MsgHdr>

**P700** 		<RptOrErr>

**P701** 			<PtyAudtTrlRpt>

**P702** 				<PtyAudtTrlOrErr>

**P703** 					<AudtTrl>

**P704** 						<Rcrd>

**P705** 							<Othr>

**P706** 							<FldNm>PostalCode</FldNm>

**P707** 							<OdFldVal>54321</OdFldVal>

**P708** 							<NewFldVal>12345</NewFldVal>

**P709** 							</Othr>

**P710** 						</Rcrd>

**P711** 						<OprTmStmp>2017-08-17T17:59:00</OprTmStmp>

**P712** 						<InstgUsr>USER1</InstgUsr>

**P713** 						<ApprvgUsr>USER2</ApprvgUsr>

**P714** 					</AudtTrl>

**P715** 				</PtyAudtTrlOrErr>

**P716** 				<PtyId>

**P717** 					<Id>

**P718** 						<Id>

**P719** 							<AnyBIC>PAYBXXYYAAA</AnyBIC>

**P720** 						</Id>

**P721** 					</Id>

**P722** 					<RspnsblPtyId>

**P723** 						<Id>

**P724** 							<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P725** 						</Id>

**P726** 					</RspnsblPtyId>

**P727** 				</PtyId>

**P728** 			</PtyAudtTrlRpt>

**P729** 		</RptOrErr>

**P730** 	</PtyAudtTrlRpt>

**P731** </Document>

