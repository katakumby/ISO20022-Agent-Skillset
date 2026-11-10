---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.2 NewCriteria <NewCrit>", "12.4.2.2.2.3 ReturnCriteria <RtrCrit>", "12.4.2.2.2.3.1 NameIndicator <NmInd>"]
file_pages: [474]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.2.3.1 NameIndicator <NmInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 474 to 474.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 474

```text
ReturnCriteria <RtrCrit> contains the following MemberReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NameIndicator <NmInd> [0..1] Indicator 474
   MemberReturnAddressIndicator <MmbRtrAdrInd> [0..1] Indicator 474
   AccountIndicator <AcctInd> [0..1] Indicator 474
   TypeIndicator <TpInd> [0..1] Indicator 474
   StatusIndicator <StsInd> [0..1] Indicator 475
   ContactReferenceIndicator <CtctRefInd> [0..1] Indicator 475
   CommunicationAddressIndicator <ComAdrInd> [0..1] Indicator 475
12.4.2.2.2.3.1  NameIndicator <NmInd>
Presence: [0..1]
Definition: Indicates whether the member name is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.2.2.2.3.2  MemberReturnAddressIndicator <MmbRtrAdrInd>
Presence: [0..1]
Definition: Indicates whether the member return address is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.2.2.2.3.3  AccountIndicator <AcctInd>
Presence: [0..1]
Definition: Indicates whether the member account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
12.4.2.2.2.3.4  TypeIndicator <TpInd>
Presence: [0..1]
Definition: Indicates whether the member type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 474 February 2025
```

