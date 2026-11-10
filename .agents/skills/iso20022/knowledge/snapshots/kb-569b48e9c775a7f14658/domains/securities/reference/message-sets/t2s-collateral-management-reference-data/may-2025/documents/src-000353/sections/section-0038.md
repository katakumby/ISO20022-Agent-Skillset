---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["Business Examples", "Collateral Management Reference Data", "reda.027.001.01 CloseLinkCreationRequest"]
content_origin: "source-transcription"
---

# reda.027.001.01 CloseLinkCreationRequest

Source: [src-000353](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Locator: heading path Business Examples / Collateral Management Reference Data / reda.027.001.01 CloseLinkCreationRequest.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P253** reda.027.001.01 CloseLinkCreationRequest

**P254** Description

**P255** The CloseLinkCreationRequest message is sent by an instructing party to the executing party to request for the creation of a close link in the executing system collateral management reference data. 

**P256** Message Instance

**P257** <ClsLkCreReq>

**P258** 	<MsgHdr>

**P259** 		<MsgId>SAMPLET2SCRECLL</MsgId>

**P260** 	</MsgHdr>

**P261** 	<ClsLk>

**P262** 		<SctyId>

**P263** 			<ISIN>XXABCDEFGHI1</ISIN>

**P264** 		</SctyId>

**P265** 		<PtyId>

**P266** 			<OrgId>

**P267** 				<Id>

**P268** 					<AnyBIC>PARXAABBXXX</AnyBIC>

**P269** 				</Id>

**P270** 			</OrgId>

**P271** 		</PtyId>

**P272** 		<CdtPrvdrId>

**P273** 			<CmbndId>

**P274** 				<Id>

**P275** 					<Id>

**P276** 						<AnyBIC>PARXAABBXXX</AnyBIC>

**P277** 					</Id>

**P278** 				</Id>

**P279** 				<RspnsblPtyId>

**P280** 					<Id>

**P281** 						<AnyBIC>NCBXAABBXXX</AnyBIC>

**P282** 					</Id>

**P283** 				</RspnsblPtyId>

**P284** 			</CmbndId>

**P285** 		</CdtPrvdrId>

**P286** 	</ClsLk>

**P287** </ClsLkCreReq>

