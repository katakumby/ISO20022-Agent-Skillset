---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.2 NewCriteria <NewCrit>", "12.4.2.2.2.3 ReturnCriteria <RtrCrit>", "12.4.2.2.2.3.5 StatusIndicator <StsInd>"]
file_pages: [475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.2.3.5 StatusIndicator <StsInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 475 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 475

```text
12.4.2.2.2.3.5  StatusIndicator <StsInd>
Presence: [0..1]
Definition: Indicates whether the member status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.2.2.2.3.6  ContactReferenceIndicator <CtctRefInd>
Presence: [0..1]
Definition: Indicates whether the contact references are requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.2.2.2.3.7  CommunicationAddressIndicator <ComAdrInd>
Presence: [0..1]
Definition: Indicates whether the communication addresses are requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 475 February 2025
```

