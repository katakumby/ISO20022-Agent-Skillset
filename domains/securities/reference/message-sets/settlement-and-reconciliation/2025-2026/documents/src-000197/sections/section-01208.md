---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.4 PartyIdentification127Choice", "35.1.18.4.2 ProprietaryIdentification <PrtryId>"]
file_pages: [1665]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.4.2 ProprietaryIdentification <PrtryId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1665 to 1665.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1665

```text
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.18.4.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 1497 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1497
   Issuer <Issr> [1..1] Text 1497
   SchemeName <SchmeNm> [0..1] Text 1497
35.1.18.5  Counterparty15Choice
Definition: Choice between buyer and seller.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Seller <Sellr> [1..1] ± C29,
C31
1665
Or}   Buyer <Buyr> [1..1] ± C29,
C31
1666
35.1.18.5.1  Seller <Sellr>
Presence: [1..1]
Definition: Party that sells goods or services, or a financial instrument.
Impacted by: C29 "SafekeepingAccountOrBlockChainAddress1Rule", C31
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1665 March 2026
```

