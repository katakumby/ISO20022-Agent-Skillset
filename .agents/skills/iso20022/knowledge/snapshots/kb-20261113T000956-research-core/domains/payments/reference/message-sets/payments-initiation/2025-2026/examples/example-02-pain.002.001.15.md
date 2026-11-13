---
template: false
document_kind: "message-example"
review_status: "reviewed"
manual_curated: true
title: "CustomerPaymentStatusReport pain.002.001.15 - 1"
domain: "payments"
source_ids: ["src-000173", "src-000177"]
message_sets: ["payments-initiation"]
message_ids: ["pain.002.001.15"]
message_families: ["pain.002"]
source_locations: [{"source_id": "src-000173", "locator": "P548–P576; T25", "heading_path": ["Business Examples", "CustomerPaymentStatusReport pain.002.001.15 - 1"]}, {"source_id": "src-000177", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pain.002.001.15; /xs:schema/xs:element[@name=\"Document\"]"}]
issue_ids: []
limitations: ["This is a supplied source example, not an invented example or current commercial event.", "Printed snippet has payload root and no namespace/Document envelope. Schema check used a separately derived envelope and qualified all source element names; original payload text is unchanged."]
participant_ids: ["participant-src-000173-example-abc-corporation-new-york", "participant-src-000173-example-bbbb-bank-new-york"]
source_editions: ["2025-2026", "March 2026"]
---

# CustomerPaymentStatusReport pain.002.001.15 - 1

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Source scenario

**P542** CustomerPaymentStatusReport pain.002.001.15 - 1

**P543** Description

**P544** As follow-up to the payment initiation by ABC Corporation, BBBBUS33 sends a CustomerPaymentStatusReport to acknowledge that the message passed technical validation and was accepted, based on the customer profile.

**P545** Business Data

**P546** CustomerPaymentStatusReport from BBBB Bank to ABC Corporation:

**P547** Message Instance

[Complete supplied Business Data table](../documents/src-000173/tables/tbl-0025.md) · [Literal extracted XML payload](../../../../../../../evidence/archived/584da4afffacfbe902622312.md)

## Validation and scope

On 2026-11-09, the literal snippet parsed as well-formed XML. A working copy with the stated message namespace and Document envelope passed validation against [src-000177](../../../../../../../raw-input/payments_initiation/pain.002.001.15.xsd). This proves the wrapped copy satisfies the supplied XSD; it does not add business-rule validation or assert table/XML value equality.

## Complete source payload

```xml
<CstmrPmtStsRpt>
	<GrpHdr>
		<MsgId>BBBB/120928-PSR/001</MsgId>
		<CreDtTm>2012-09-28T14:09:00</CreDtTm>
		<InitgPty>
			<Nm>ABC Corporation</Nm>
			<PstlAdr>
				<StrtNm>Times Square</StrtNm>
				<BldgNb>7</BldgNb>
				<PstCd>NY 10036</PstCd>
				<TwnNm>New York</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</InitgPty>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</DbtrAgt>
	</GrpHdr>
	<OrgnlGrpInfAndSts>
		<OrgnlMsgId>ABC/120928/CCT001</OrgnlMsgId>
		<OrgnlMsgNmId>pain.001.001.13</OrgnlMsgNmId>
		<OrgnlCreDtTm>2012-09-28T14:07:00</OrgnlCreDtTm>
		<OrgnlNbOfTxs>3</OrgnlNbOfTxs>
		<OrgnlCtrlSum>11500000</OrgnlCtrlSum>
		<GrpSts>ACCP</GrpSts>
	</OrgnlGrpInfAndSts>
</CstmrPmtStsRpt>
```

<!-- EXAMPLE-PARTICIPANT-abc-corporation-new-york -->
[ABC Corporation, New York](../../../../../../../shared/reference/participants/participant-src-000173-example-abc-corporation-new-york.md) — Holds account 00125574999 and instructs BBBB Bank New York to pay three invoices; receives technical/customer-profile acceptance status. (P322–331; P544–546; T24; T25)
<!-- /EXAMPLE-PARTICIPANT-abc-corporation-new-york -->

<!-- EXAMPLE-PARTICIPANT-bbbb-bank-new-york -->
[BBBB Bank, New York](../../../../../../../shared/reference/participants/participant-src-000173-example-bbbb-bank-new-york.md) — Receives ABC Corporation initiation and sends CustomerPaymentStatusReport after technical validation/customer-profile acceptance. (P329–331; P544–546; T24–T25)
<!-- /EXAMPLE-PARTICIPANT-bbbb-bank-new-york -->
