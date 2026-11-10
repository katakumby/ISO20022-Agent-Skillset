---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.8 Person Identification", "4.1.8.1 Contact13", "4.1.8.1.1 NamePrefix <NmPrfx>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.8.1.1 NamePrefix <NmPrfx>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
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
4.1.8.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 147
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
4.1.8.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 151
4.1.8.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 133 December 2025
```

