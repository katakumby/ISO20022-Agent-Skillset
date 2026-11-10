---
template: false
document_kind: "message-example"
title: "FIToFIPaymentReversal pacs.007.001.14"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000168"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.007.001.14"]
message_families: ["pacs.007"]
source_locations: [{"source_id": "src-000162", "locator": "P1168–P1258; T34", "heading_path": ["Business Examples", "FIToFIPaymentReversal pacs.007.001.14"]}, {"source_id": "src-000168", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-bbbbus39", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFIPaymentReversal pacs.007.001.14

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P1160** FIToFIPaymentReversal pacs.007.001.14

**P1161** Description

**P1162** On 6 July 2015, AAAAUS29 finds out that the FIToFICustomerDirectDebit message it sent to ABABUS23 on 28 June 2015, for the collection of USD 1025 from debtor Jones, was a duplicated payment instruction. As the requested collection date was 13 July 2015, AAAAUS29 decides to send an FIToFIPaymentReversal message to its correspondent ABABUS23, giving the reason for the reversal.

**P1163** Any potential charges related to the reversal will be settled outside of the message, that is as part of the monthly billing process.

**P1164** The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

**P1165** Business Data

**P1166** FIToFIPaymentReversal from AAAAUS29 to ABABUS23:

**P1167** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0034.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-07.xml) · [Source example flow](../flows/example-src-000162-07.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | InstgAgt | /FIToFIPmtRvsl/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | InstdAgt | /FIToFIPmtRvsl/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr | /FIToFIPmtRvsl/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |
| [BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus39.md) | DbtrAgt | /FIToFIPmtRvsl/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr | /FIToFIPmtRvsl/TxInf/OrgnlTxRef/Cdtr/Pty/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14 and wrapped in Document passed the exact supplied XSD src-000168. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <OrgnlEndToEnd> is retained literally; corresponding instance vocabulary uses OrgnlEndToEndId. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFIPmtRvsl>
	<GrpHdr>
		<MsgId>AAAAUS29-REVERSAL/0012</MsgId>
		<CreDtTm>2015-07-06T10:35:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<IntrBkSttlmDt>2015-07-06</IntrBkSttlmDt>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>ABABUS23</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>AAAA120628-123v</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<TxInf>
		<RvslId>AAAAUS29_REV2563</RvslId>
		<OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>
		<OrgnlTxId>AAAAUS29/150628/ad458</OrgnlTxId>
		<RvsdIntrBkSttlmAmt Ccy="USD">1025</RvsdIntrBkSttlmAmt>
		<RvsdInstdAmt Ccy="USD">1025</RvsdInstdAmt>
		<RvslRsnInf>
			<Orgtr>
				<Id>
					<OrgId>
						<AnyBIC>AAAAUS29</AnyBIC>
					</OrgId>
				</Id>
			</Orgtr>
			<Rsn>
				<Cd>AM05</Cd>
			</Rsn>
		</RvslRsnInf>
		<OrgnlTxRef>
			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
			<ReqdColltnDt>2015-07-13</ReqdColltnDt>
			<MndtRltdInf>
				<DrctDbtMndt>
					<MndtId>VIRGAY123</MndtId>
				</DrctDbtMndt>
			</MndtRltdInf>
			<Dbtr>
				<Pty>
					<Nm>Jones</Nm>
					<PstlAdr>
						<StrtNm>Hudson Street</StrtNm>
						<BldgNb>19</BldgNb>
						<PstCd>NJ 07302</PstCd>
						<TwnNm>Jersey City</TwnNm>
						<Ctry>US</Ctry>
					</PstlAdr>
				</Pty>	
			</Dbtr>
			<DbtrAcct>
				<Id>
					<Othr>
						<Id>123456</Id>
					</Othr>
				</Id>
			</DbtrAcct>
			<DbtrAgt>
				<FinInstnId>
					<BICFI>BBBBUS39</BICFI>
				</FinInstnId>
			</DbtrAgt>
			<Cdtr>
				<Pty>
					<Nm>Virgay</Nm>
					<PstlAdr>
						<StrtNm>Virginia Lane</StrtNm>
						<BldgNb>36</BldgNb>
						<PstCd>NJ 07311</PstCd>
						<TwnNm>Jersey City</TwnNm>
						<Ctry>US</Ctry>
					</PstlAdr>
				</Pty>
			</Cdtr>
		</OrgnlTxRef>
	</TxInf>
</FIToFIPmtRvsl>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-07.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
