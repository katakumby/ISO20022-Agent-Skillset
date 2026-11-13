---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Report - reda.021.001.01"]
content_origin: "source-transcription"
---

# Securities Account Report - reda.021.001.01

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Report - reda.021.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P524** Securities Account Report - reda.021.001.01

**P525** Description

**P526** The Securities Account Report message can be used as answer for:

**P527** Securities Account Reference Data Query;

**P528** Securities Account List Query.

**P529** performed using the Securities Account Query. This example shows the answer to the Securities Account List Query described in the chapter 7.5. The query returns only one securities account:

**P530** Securities Account Identification: SECACCCSDPXXYYAAA

**P531** Account owner Parent BIC: CSDAXXYYAAA

**P532** Account owner Party BIC: CSDPXXYYAAA 

**P533** End investor flag: NONE

**P534** Pricing scheme: SACC

**P536** Message Instance

**P537** <Document>

**P538** 	<SctiesAcctRpt>

**P539** 		<MsgHdr>

**P540** 			<MsgId>NONREF</MsgId>

**P541** 			<OrgnlBizQry>

**P542** 				<MsgId>SAMPLESALIQUERY</MsgId>

**P543** 			</OrgnlBizQry>

**P544** 		</MsgHdr>

**P545** 		<Pgntn>

**P546** 			<PgNb>1</PgNb>

**P547** 			<LastPgInd>true</LastPgInd>

**P548** 		</Pgntn>

**P549** 		<RptOrErr>

**P550** 			<SctiesAcctRpt>

**P551** 				<SctiesAcctId>

**P552** 					<Id>SECACCCSDPXXYYAAA</Id>

**P553** 				</SctiesAcctId>

**P554** 				<SctiesAcctOrErr>

**P555** 					<SctiesAcct>

**P556** 						<AcctOwnr>

**P557** 							<Id>

**P558** 								<Id>

**P559** 									<AnyBIC>CSDPXXYYAAA</AnyBIC>

**P560** 								</Id>

**P561** 							</Id>

**P562** 							<RspnsblPtyId>

**P563** 								<Id>

**P564** 									<AnyBIC>CSDAXXYYAAA</AnyBIC>

**P565** 								</Id>

**P566** 							</RspnsblPtyId>

**P567** 						</AcctOwnr>

**P568** 						<EndInvstrFlg>NONE</EndInvstrFlg>

**P569** 						<PricgSchme>SACC</PricgSchme>

**P570** 					</SctiesAcct>

**P571** 				</SctiesAcctOrErr>

**P572** 			</SctiesAcctRpt>

**P573** 		</RptOrErr>

**P574** 	</SctiesAcctRpt>

**P575** </Document>

