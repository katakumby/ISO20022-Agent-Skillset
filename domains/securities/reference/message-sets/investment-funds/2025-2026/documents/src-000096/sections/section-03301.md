---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.2 AdditionalReference2"]
file_pages: [4538]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.2 AdditionalReference2

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4538 to 4538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4538

```text
Datatype: "Max35Text" on page 5403
66.1.23.2  AdditionalReference2
Definition: References a related message or provides another reference, such as a pool reference,
linking a set of messages. The party which issued the related reference may be the Sender of the
referenced message or a party other than the Sender.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
66.1.23.2.1  Reference <Ref>
Presence: [1..1]
Definition: Business reference of a message assigned by the party issuing the message. This reference
must be unique amongst all messages of the same name sent by the same party.
Datatype: "Max35Text" on page 5403
66.1.23.2.2  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Issuer of the reference.
ReferenceIssuer <RefIssr> contains one of the following elements (see "PartyIdentification1Choice"
on page 4893 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4894
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4894
Or}   NameAndAddress <NmAndAdr> [1..1]  4894
     Name <Nm> [1..1] Text 4895
     Address <Adr> [0..1] ± 4895
66.1.23.2.3  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of a message.
Datatype: "Max35Text" on page 5403
66.1.23.3  GenericIdentification7
Definition: Information expressed in a proprietary manner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4538 May 2026
```

