---
template: false
document_kind: "message-example"
title: "PaymentReturn pacs.004.001.15 - 1"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000167"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
source_locations: [{"source_id": "src-000162", "locator": "P844–P899; T30", "heading_path": ["Business Examples", "PaymentReturn pacs.004.001.15 - 1", "First PaymentReturn"]}, {"source_id": "src-000167", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-bbbbie2d", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-0785746"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# PaymentReturn pacs.004.001.15 - 1

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P836** PaymentReturn pacs.004.001.15 - 1

**P837** This example covers two PaymentReturn messages. The first PaymentReturn message is sent by CCCC Bank to BBBB Bank. The second PaymentReturn message is sent by BBBB Bank to AAAA Bank.

**P838** First PaymentReturn

**P839** Description

**P840** On receipt of an FIToFIPaymentCancellationRequest message from BBBB Bank, CCCC Bank checks with Seed Inc. whether it is willing to return the credited funds. Seed Inc. accepts to return the amount credited onto its account (EUR 74850) without requesting compensation. CCCC Bank sends a PaymentReturn message to BBBB Bank.

**P841** Business Data

**P842** PaymentReturn from CCCC Bank to BBBB Bank:

**P843** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0030.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-03.xml) · [Source example flow](../flows/example-src-000162-03.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | InstgAgt | /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | InstdAgt | /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | Agt | /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-0785746.md) | Orgtr | /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15 and wrapped in Document passed the exact supplied XSD src-000167. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table ReturnIdentification CCCC/151122-PR007/1; XML RtrId CCCC/151122-PR007.

## Complete source payload

```xml
<PmtRtr>
	<GrpHdr>
		<MsgId>CCCC/151122-PR007</MsgId>
		<CreDtTm>2015-11-22T10:37:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>CLRG</SttlmMtd>
			<ClrSys>
				<Prtry>CBJ</Prtry>
			</ClrSys>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>CCCCIE2D</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>BBBBIE2D</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>BBBB/151109-CBJ056</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-11-09T10:13:00</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<TxInf>
		<RtrId>CCCC/151122-PR007</RtrId>
		<OrgnlInstrId>BBBB/151109-CBJ056/1</OrgnlInstrId>
		<OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>
		<OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>
		<OrgnlIntrBkSttlmAmt Ccy="EUR">74900</OrgnlIntrBkSttlmAmt>
		<RtrdIntrBkSttlmAmt Ccy="EUR">74750</RtrdIntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-11-22</IntrBkSttlmDt>
		<RtrdInstdAmt Ccy="EUR">74850</RtrdInstdAmt>
		<ChrgBr>CRED</ChrgBr>
		<ChrgsInf>
			<Amt Ccy="EUR">100</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>CCCCIE2D</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
		<RtrRsnInf>
			<Orgtr>
				<Nm>Seed Inc.</Nm>
			</Orgtr>
			<Rsn>
				<Cd>NARR</Cd>
			</Rsn>
			<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>
		</RtrRsnInf>
	</TxInf>
</PmtRtr>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-03.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
