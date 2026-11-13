---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.3 ReturnCriteria <RtrCrit>", "30.4.2.2.2.3.9 FrequencyIndicator <FrqcyInd>"]
file_pages: [704]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.3.9 FrequencyIndicator <FrqcyInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 704 to 704.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 704

```text
30.4.2.2.2.3.9  FrequencyIndicator <FrqcyInd>
Presence: [0..1]
Definition: Indicates whether the frequency is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.10  ExecutionTypeIndicator <ExctnTpInd>
Presence: [0..1]
Definition: Indicates whether the execution type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.11  ValidityFromIndicator <VldtyFrInd>
Presence: [0..1]
Definition: Indicates whether the account standing order is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.12  ValidToIndicator <VldToInd>
Presence: [0..1]
Definition: Indicates whether the account owner information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.13  LinkSetIdentificationIndicator <LkSetIdInd>
Presence: [0..1]
Definition: Indicates whether the link set identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.14  LinkSetOrderIdentificationIndicator <LkSetOrdrIdInd>
Presence: [0..1]
Definition: Indicates whether the identification of a standing order within a link set is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 704 February 2025
```

