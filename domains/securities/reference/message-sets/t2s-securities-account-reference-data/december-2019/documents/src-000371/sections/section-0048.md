---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Creation Request - reda.018.001.01"]
content_origin: "source-transcription"
---

# Securities Account Creation Request - reda.018.001.01

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Creation Request - reda.018.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P329** Securities Account Creation Request - reda.018.001.01

**P330** Description

**P331** The instructing Party wants to create a new securities account with the following information:

**P332** Account owner Parent BIC: CSDAXXYYAAA

**P333** Account owner Party BIC: CSDPXXYYAAA 

**P334** Security account identification: SECACCCSDPXXYYAAA

**P335** Account Type: CSDP

**P336** Opening date: 2019-01-01

**P337** Hold indicator: true

**P338** Negative position indicator: false

**P339** End investor flag: NONE

**P340** Pricing scheme: SACC

**P341** Message Instance

**P342** <Document>

**P343** <Document>

**P344** 	<SctiesAcctCreReq>

**P345** 		<MsgHdr>

**P346** 			<MsgId>SAMPLECRESAC</MsgId>

**P347** 		</MsgHdr>

**P348** 		<SctiesAcct>

**P349** 			<AcctOwnr>

**P350** 				<Id>

**P351** 					<Id>

**P352** 						<AnyBIC>CSDPXXYYAAA</AnyBIC>

**P353** 					</Id>

**P354** 				</Id>

**P355** 				<RspnsblPtyId>

**P356** 					<Id>

**P357** 						<AnyBIC>CSDAXXYYAAA</AnyBIC>

**P358** 					</Id>

**P359** 				</RspnsblPtyId>

**P360** 			</AcctOwnr>

**P361** 			<Id>SECACCCSDPXXYYAAA</Id>

**P362** 			<Tp>

**P363** 				<Cd>CSDP</Cd>

**P364** 			</Tp>

**P365** 			<OpngDt>2019-01-01</OpngDt>

**P366** 			<HldInd>true</HldInd>

**P367** 			<NegPos>false</NegPos>

**P368** 			<EndInvstrFlg>NONE</EndInvstrFlg>

**P369** 			<PricgSchme>SACC</PricgSchme>

**P370** 		</SctiesAcct>

**P371** 	</SctiesAcctCreReq>

**P372** </Document></Document>

