---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.8 Person Identification"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.8 Person Identification

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 132 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 133
   Name <Nm> [0..1] Text 133
   PhoneNumber <PhneNb> [0..1] Text 133
   MobileNumber <MobNb> [0..1] Text 134
   FaxNumber <FaxNb> [0..1] Text 134
   URLAddress <URLAdr> [0..1] Text 134
   EmailAddress <EmailAdr> [0..1] Text 134
   EmailPurpose <EmailPurp> [0..1] Text 134
   JobTitle <JobTitl> [0..1] Text 134
   Responsibility <Rspnsblty> [0..1] Text 134
   Department <Dept> [0..1] Text 134
   Other <Othr> [0..*]  135
     ChannelType <ChanlTp> [1..1] Text 135
     Identification <Id> [0..1] Text 135
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 135
4.1.8 Person Identification
4.1.8.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 132 December 2025
```

