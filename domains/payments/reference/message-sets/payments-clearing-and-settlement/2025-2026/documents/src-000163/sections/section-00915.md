---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.15 Person Identification", "10.1.15.1 Contact13", "10.1.15.1.1 NamePrefix <NmPrfx>"]
file_pages: [1210]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.15.1.1 NamePrefix <NmPrfx>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1210 to 1210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1210

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 1210
   Name <Nm> [0..1] Text 1210
   PhoneNumber <PhneNb> [0..1] Text 1210
   MobileNumber <MobNb> [0..1] Text 1211
   FaxNumber <FaxNb> [0..1] Text 1211
   URLAddress <URLAdr> [0..1] Text 1211
   EmailAddress <EmailAdr> [0..1] Text 1211
   EmailPurpose <EmailPurp> [0..1] Text 1211
   JobTitle <JobTitl> [0..1] Text 1211
   Responsibility <Rspnsblty> [0..1] Text 1211
   Department <Dept> [0..1] Text 1211
   Other <Othr> [0..*]  1212
     ChannelType <ChanlTp> [1..1] Text 1212
     Identification <Id> [0..1] Text 1212
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 1212
10.1.15.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 1235
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
10.1.15.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 1244
10.1.15.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1210 March 2026
```

