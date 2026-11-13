---
template: false
document_kind: "message-example"
title: "PaymentReturn pacs.004.001.15 - 2"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000167"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
source_locations: [{"source_id": "src-000162", "locator": "P975–P1060; T32", "heading_path": ["Business Examples", "PaymentReturn pacs.004.001.15 - 2", "First PaymentReturn"]}, {"source_id": "src-000167", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-ababus23", "participant-src-000162-example-bbbbus39", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# PaymentReturn pacs.004.001.15 - 2

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P967** PaymentReturn pacs.004.001.15 - 2

**P968** This example covers two PaymentReturn messages. The first PaymentReturn message is sent by BBBBUS39 to ABABUS23. The second PaymentReturn message is sent by ABABUS23 to AAAAUS29.

**P969** First PaymentReturn

**P970** Description

**P971** On 28 June 2015, upon receipt of a direct debit instruction received from ABABUS23 for the collection of USD 1025, and after having checked the instruction, BBBBUS39 realises that the account specified for debtor Jones does not allow direct debits. BBBBUS39 therefore decides to send a PaymentReturn message to ABABUS23, specifying the reason, and taking charges for USD 50.

**P972** Business Data

**P973** PaymentReturn from BBBBUS39 to ABABUS23:

**P974** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0032.md) · [Literal XML payload](../../../../../../../evidence/archived/3167595f4275f2487f39614a.md) · [Source example flow](../flows/example-src-000162-05.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus39.md) | InstgAgt | /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | InstdAgt | /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus39.md) | Agt | /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr | /PmtRtr/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr | /PmtRtr/TxInf/OrgnlTxRef/Cdtr/Pty/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15 and wrapped in Document passed the exact supplied XSD src-000167. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table MsgId BBBBUS39-RETURN-0213; XML BBBBUS39-RETURN-0123.
- Table OriginalEndToEndIdentification <OrgnlEndToEnd> VA060327/0123; instance assigns that value to OrgnlInstrId, not OrgnlEndToEndId.
- Table tag <RtnId> is retained literally; corresponding instance vocabulary uses RtrId. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<PmtRtr>
	<GrpHdr>
		<MsgId>BBBBUS39-RETURN-0123</MsgId>
		<CreDtTm>2015-06-29T11:15:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INGA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS39</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>ABABUS23</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>ABABUS23-589cd</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-06-28T15:02:00</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<TxInf>
		<RtrId>AB/RETURN765</RtrId>
		<OrgnlInstrId>VA060327/0123</OrgnlInstrId>
		<RtrdIntrBkSttlmAmt Ccy="USD">975</RtrdIntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-07-29</IntrBkSttlmDt>
		<ChrgBr>CRED</ChrgBr>
		<ChrgsInf>
			<Amt Ccy="USD">50</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>BBBBUS39</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
		<RtrRsnInf>
			<Orgtr>
				<Id>
					<OrgId>
						<AnyBIC>BBBBUS39</AnyBIC>
					</OrgId>
				</Id>
			</Orgtr>
			<Rsn>
				<Cd>AG01</Cd>
			</Rsn>
		</RtrRsnInf>
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
</PmtRtr>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-05.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
