---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.13 Payment"]
file_pages: [1202]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.13 Payment

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1202 to 1202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1202

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 1209 for details)
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
10.1.13 Payment
10.1.13.1  SettlementTimeRequest2
Definition: Provides information on the requested settlement time(s) of the payment instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CLSTime <CLSTm> [0..1] Time 1202
   TillTime <TillTm> [0..1] Time 1203
   FromTime <FrTm> [0..1] Time 1203
   RejectTime <RjctTm> [0..1] Time 1203
10.1.13.1.1  CLSTime <CLSTm>
Presence: [0..1]
Definition: Time by which the amount of money must be credited, with confirmation, to the CLS Bank's
account at the central bank.
Usage: Time must be expressed in Central European Time (CET).
Datatype: "ISOTime" on page 1247
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1202 March 2026
```

