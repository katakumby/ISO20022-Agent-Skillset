---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Report Query Request - admi.005.001"]
content_origin: "source-transcription"
---

# Report Query Request - admi.005.001

Source: [src-000343](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Locator: heading path Examples / Report Query Request - admi.005.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P197** Report Query Request - admi.005.001

**P198** Description

**P199** The Report Query Request message is sent by a System Member to a System Transaction Administrator. In this example a “Complete Statement of pending Amendment Instructions for Intra-Position Movements and Settlement Instruction report” identified via code “CPAP” dated 2017-08-13 is requested from Party “ACCTOWNRXXX” belonging to Parent BIC “ACCTSVCRXXX”. 

**P200** Search criteria which are defined:

**P201** Report Name: Complete Statement of pending Amendment Instructions …”CPAP”

**P202** Party Identification via two BICs: “ACCTOWNRXXX” and “ACCTSVCRXXX”

**P203** Date when the Report was produced:  2017-08-13

**P204** Message Instance

**P206** 	<RptQryReq>

**P207** 		<MsgHdr>

**P208** 			<MsgId>T2SREPORTQUERY01</MsgId>

**P209** 		</MsgHdr>

**P210** 		<RptQryCrit>

**P211** 			<SchCrit>

**P212** 				<RptNm>CPAP</RptNm>

**P213** 				<PtyId>

**P214** 				  <Id>

**P215** 					<AnyBIC>ACCTOWNRXXX</AnyBIC>

**P216** 				  </Id>					

**P217** 				</PtyId>

**P218** 				<RspnsblPtyId>

**P219** 					<Id>

**P220** 						<AnyBIC>ACCTSVCRXXX</AnyBIC>

**P221** 					</Id>					

**P222** 				</RspnsblPtyId>

**P223** 				<DtSch>

**P224** 					<EQDt>2017-08-13</EQDt>

**P225** 				</DtSch>

**P226** 			</SchCrit>

**P227** 		</RptQryCrit>

**P228** 	</RptQryReq>	

