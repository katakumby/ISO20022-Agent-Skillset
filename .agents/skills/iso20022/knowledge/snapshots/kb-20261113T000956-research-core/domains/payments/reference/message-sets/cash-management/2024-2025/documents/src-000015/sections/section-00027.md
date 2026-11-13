---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.2.3.7 BilateralBalanceReturnCriteria <BilBalRtrCrit>", "2.4.2.2.2.3.7.5 NumberOfPaymentsIndicator <NbOfPmtsInd>"]
file_pages: [46, 47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.3.7.5 NumberOfPaymentsIndicator <NbOfPmtsInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 46 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
2.4.2.2.2.3.7.5  NumberOfPaymentsIndicator <NbOfPmtsInd>
Presence: [1..1]
Definition: Indicates whether the number of payment is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.8  StandingOrderIndicator <StgOrdrInd>
Presence: [0..1]
Definition: Indicates whether the account standing order is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.9  AccountOwnerIndicator <AcctOwnrInd>
Presence: [0..1]
Definition: Indicates whether the account owner information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.10  AccountServicerIndicator <AcctSvcrInd>
Presence: [0..1]
Definition: Indicates whether the account servicer information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 46 February 2025
```

## File page 47

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 47 February 2025
```

