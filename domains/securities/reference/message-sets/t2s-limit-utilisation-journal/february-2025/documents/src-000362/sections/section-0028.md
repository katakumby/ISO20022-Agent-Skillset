---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["Business Examples", "Example #2: Operational Errors", "Message example"]
content_origin: "source-transcription"
---

# Message example

Source: [src-000362](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Locator: heading path Business Examples / Example #2: Operational Errors / Message example.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P317** Message example

**P318** Limit Utilisation Journal Query - camt.064.001.01

**P320**   <LmtUtlstnJrnlQry>

**P321** 	 <MsgHdr>

**P322** 		<MsgId>REFKLM</MsgId>

**P323** 	 </MsgHdr>

**P324** 	 <SchCrit>

**P325** 		<LmtTp>ACOL</LmtTp>

**P326** 		<JrnlActvtyDt>2015-01-21</JrnlActvtyDt>

**P327** 		<BilLmtCtrPtyId>

**P328** 				<Id>

**P329** 					<Id>

**P330** 						<AnyBIC> PBKHBIC0XXX </AnyBIC>

**P331** 					</Id>

**P332** 				</Id>

**P333** 				<RspnsblPtyId>

**P334** 					<Id>

**P335** 						<AnyBIC> CBHHBIC2XXX </AnyBIC>

**P336** 					</Id>

**P337** 				</RspnsblPtyId>

**P338** 			</BilLmtCtrPtyId>

**P339** 	 </SchCrit>

**P340** 	</LmtUtlstnJrnlQry>

**P342** Limit Utilisation Journal Report - camt.065.001.01

**P344** <LmtUtlstnJrnlRpt>

**P345** 	<MsgHdr>

**P346** 		<MsgId>NONREF</MsgId>

**P347** 		<OrgnlBizInstr>

**P348** 			<MsgId>REFKLM</MsgId>

**P349** 		</OrgnlBizInstr>

**P350** 	</MsgHdr>

**P351** 	<Pgntn>

**P352** 		<PgNb>1</PgNb>

**P353** 		<LastPgInd>true</LastPgInd>

**P354** 	</Pgntn>

**P355** 		<RptOrErr>

**P356** 		  <OprlErr>

**P357** 			  <Err>

**P358** 			    <Prtry>Q065</Prtry>

**P359** 			  </Err>

**P360** 			  <Desc>The specified business date is in the future</Desc>

**P361** 		  </OprlErr>

**P362** 		</RptOrErr>

**P363** 	</LmtUtlstnJrnlRpt>

