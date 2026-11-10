---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Business Examples", "Party Modification Request - reda.022.001"]
content_origin: "source-transcription"
---

# Party Modification Request - reda.022.001

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Business Examples / Party Modification Request - reda.022.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P356** Party Modification Request - reda.022.001

**P357** Description

**P358** In this example, the instructing party wants to update the Street name and the building number of the Party BANKXXYYAAA:

**P359** Party ID: BANKXXYYAAA

**P360** Responsible Party ID: NCBAXXYYAAA

**P361** New Street name: Largo Guido Carli

**P362** Building number: 01

**P363** Address Valid From: 2017-08-23

**P364** Message Instance

**P365**  

**P366** <Document>

**P367** 	<PtyModReq>

**P368** 		<MsgHdr>

**P369** 			<MsgId>SAMPLEPARTYUPD</MsgId>

**P370** 		</MsgHdr>

**P371** 		<SysPtyId>

**P372** 			<Id>

**P373** 				<Id>

**P374** 					<AnyBIC>BANKXXYYAAA</AnyBIC>

**P375** 				</Id>

**P376** 			</Id>

**P377** 			<RspnsblPtyId>

**P378** 				<Id>

**P379** 					<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P380** 				</Id>

**P381** 			</RspnsblPtyId>

**P382** 		</SysPtyId>

**P383** 		<Mod>

**P384** 			<ScpIndctn>UPDT</ScpIndctn>

**P385** 			<ReqdMod>

**P386** 				<PtyAdr>

**P387** 					<StrtNm>Largo Guido Carli</StrtNm>

**P388** 					<BldgNb>01</BldgNb>

**P389** 					<VldFr>2017-08-23</VldFr>

**P390** 				</PtyAdr>

**P391** 			</ReqdMod>

**P392** 		</Mod>

**P393** 	</PtyModReq>

**P394** </Document>

**P395**   


