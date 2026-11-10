---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.10 ResponseStatus <RspnSts>", "35.1.29.22.10.1 Code <Cd>"]
file_pages: [1914]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.10.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1914 to 1914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1914

```text
Definition: Provides the status of the received collateral message (collateral claim, a collateral proposal
or a proposal/request for collateral substitution) from a collateral management perspective.
ResponseStatus <RspnSts> contains one of the following ResponseStatus5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1914
Or}   Proprietary <Prtry> [1..1] ± 1914
35.1.29.22.10.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of the received collateral message (collateral claim, a collateral proposal
or a proposal/request for collateral substitution) from a collateral management perspective.
Datatype: "ResponseStatus1Code" on page 2136
CodeName Name Definition
ACCP PartlyAccepted Part of the collateral is accepted, a part
rejected.
ACCT Accepted Claim, substitution, proposal is fully
accepted.
REJT Rejected Claim, substitution, proposal is fully
rejected.
SUBR SubstitutionAccepted Party A agrees with the return part of the
substitution and accepts to wait for the
proposal of the new collateral.
35.1.29.22.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of the received collateral message (collateral claim, a collateral proposal
or a proposal/request for collateral substitution) from a collateral management perspective.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.11  ReplacementProcessingStatus <RplcmntPrcgSts>
Presence: [1..1]
Definition: Provides the processing status of the replacement request.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1914 March 2026
```

