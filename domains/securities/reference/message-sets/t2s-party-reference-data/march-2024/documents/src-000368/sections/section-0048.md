---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Business Examples", "Party Report - reda.017.001"]
content_origin: "source-transcription"
---

# Party Report - reda.017.001

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Business Examples / Party Report - reda.017.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P539** Party Report - reda.017.001

**P540** Description

**P541** The PartyReport (reda.017) message can be used as answer for:

**P542** Party Reference Data Query;

**P543** Party List Query;

**P544** Restricted Party Query

**P545** performed using the Party Query message (reda.015). This example shows the answer to the Party List Query described in the chapter 7.5. The query returns only one Party: 

**P546** Party ID: BANKXXYYAAA

**P547** Responsible Party ID: NCBAXXYYAAA

**P548** Party name: SAMPLE PAYMENT BANK

**P549** Party short name: SAMPLE

**P550** Message Instance

**P551** <Document>

**P552** 	<PtyRpt>

**P553** 		<MsgHdr>

**P554** 			<MsgId>NONREF</MsgId>

**P555** 			<OrgnlBizQry>

**P556** 				<MsgId>SAMPLEPTYLISQUE</MsgId>

**P557** 			</OrgnlBizQry>

**P558** 		</MsgHdr>

**P559** 		<RptOrErr>

**P560** 			<PtyRpt>

**P561** 				<PtyId>

**P562** 					<Id>

**P563** 						<Id>

**P564** 							<AnyBIC>BANKXXYYAAA</AnyBIC>

**P565** 						</Id>

**P566** 					</Id>

**P567** 					<RspnsblPtyId>

**P568** 						<Id>

**P569** 							<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P570** 						</Id>

**P571** 					</RspnsblPtyId>

**P572** 				</PtyId>

**P573** 				<PtyOrErr>

**P574** 					<SysPty>

**P575** 						<Nm>

**P576** 							<Nm>SAMPLE PAYMENT BANK</Nm>

**P577** 							<ShrtNm>SAMPLE</ShrtNm>

**P578** 						</Nm>

**P579** 					</SysPty>

**P580** 				</PtyOrErr>

**P581** 			</PtyRpt>

**P582** 		</RptOrErr>

**P583** 	</PtyRpt>

**P584** </Document>

**P585**   


