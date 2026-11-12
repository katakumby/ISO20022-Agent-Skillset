---
template: false
document_kind: "message-example"
title: "Second FinancialInstitutionCreditTransfer"
review_status: "reviewed"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000170"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2290–P2351; T44", "heading_path": ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2", "Second FinancialInstitutionCreditTransfer"]}, {"source_id": "src-000170", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaafrpp", "participant-src-000162-example-bbbbittt", "participant-src-000162-example-ccccsess", "participant-src-000162-example-ddddlull", "participant-src-000162-example-ffffsess"]
issue_ids: []
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Second FinancialInstitutionCreditTransfer

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P2284** Second FinancialInstitutionCreditTransfer

**P2285** Description

**P2286** On 22 October 2015 CCCC forwards the FinancialInstitutionCreditTransfer to the next party in the chain FFFF through the Swedish RTGS system RIX.

**P2287** Business Data

**P2288** The second FinancialInstitutionCreditTransfer message, from CCCCSESS to FFFFSESS:

**P2289** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0044.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-17.xml) · [Source example flow](../flows/example-src-000162-16.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [CCCCSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccsess.md) | InstgAgt | /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [FFFFSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ffffsess.md) | InstdAgt | /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [AAAAFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaafrpp.md) | Dbtr | /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [DDDDLULL](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddlull.md) | CdtrAgt | /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [BBBBITTT](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbittt.md) | Cdtr | /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13 and wrapped in Document passed the exact supplied XSD src-000170. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

## Complete source payload

```xml
<FICdtTrf>
	<GrpHdr>
		<MsgId>CCCC/151022-SSK/075</MsgId>
		<CreDtTm>2015-10-22T09:00:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>CLRG</SttlmMtd>
			<ClrSys>
				<Cd>SSK</Cd>
			</ClrSys>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>CCCCSESS</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>FFFFSESS</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>CCCC/151022-SSK/075/1</InstrId>
			<EndToEndId>BBBBTT4148AAAAPP</EndToEndId>
			<TxId>AAAA/151020-SEK/005/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>
		<Dbtr>
			<FinInstnId>
				<BICFI>AAAAFRPP</BICFI>
			</FinInstnId>
		</Dbtr>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>DDDDLULL</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<CdtrAgtAcct>
			<Id>
				<Othr>
					<Id>24538877443</Id>
				</Othr>
			</Id>
		</CdtrAgtAcct>
		<Cdtr>
			<FinInstnId>
				<BICFI>BBBBITTT</BICFI>
			</FinInstnId>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>995566ZZ876</Id>
				</Othr>
			</Id>
			<Ccy>SEK</Ccy>
			</CdtrAcct>
	</CdtTrfTxInf>
</FICdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-16.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
