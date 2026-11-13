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
source_locations: [{"source_id": "src-000162", "locator": "P2154–P2199; T42", "heading_path": ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 1", "Second FinancialInstitutionCreditTransfer"]}, {"source_id": "src-000170", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ccccjpjt"]
issue_ids: []
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Second FinancialInstitutionCreditTransfer

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P2148** Second FinancialInstitutionCreditTransfer

**P2149** Description

**P2150** On receipt of the instruction of BBBB Bank, CCCC Bank forwards the FinancialInstitutionCreditTransfer to the creditor agent AAAAJPJT. CCCC Bank holds multiple accounts with AAAAJPJT, and specifies that account 3451571 has to be used for reimbursement.

**P2151** Business Data

**P2152** FinancialInstitutionCreditTransfer from CCCCJPJT to AAAAJPJT:

**P2153** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0042.md) · [Literal XML payload](../../../../../../../evidence/archived/1018fc047c1803c702d1edb1.md) · [Source example flow](../flows/example-src-000162-14.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | InstgAgt | /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | InstdAgt | /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Dbtr | /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr | /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13 and wrapped in Document passed the exact supplied XSD src-000170. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

## Complete source payload

```xml
<FICdtTrf>
	<GrpHdr>
		<MsgId>CCCC/150929-FICT/743</MsgId>
		<CreDtTm>2015-09-29T08:00:10</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
			<SttlmAcct>
				<Id>
					<Othr>
						<Id>3451571</Id>
					</Othr>
				</Id>
			</SttlmAcct>
		</SttlmInf>
	<InstgAgt>
			<FinInstnId>
				<BICFI>CCCCJPJT</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>AAAAJPJT</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>CCCC/150929-FICT/743/1</InstrId>
			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>
			<TxId>BBBB/150928-CCT/JPY/123/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
		<Dbtr>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</Dbtr>
		<Cdtr>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</Cdtr>
	</CdtTrfTxInf>
</FICdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-14.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
