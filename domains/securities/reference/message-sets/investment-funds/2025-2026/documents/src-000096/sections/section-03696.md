---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.17 ContactAttributes6"]
file_pages: [4964]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.17 ContactAttributes6

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4964 to 4964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4964

```text
Intermediary <Intrmy> contains the following elements (see "Intermediary46" on page 5023 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  5023
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 5024
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 5024
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 5024
   Account <Acct> [0..1]  5024
     Identification <Id> [0..1] Text 5025
     AccountServicer <AcctSvcr> [1..1] ± 5025
   WaivedTrailerCommissionIndicator <WvdTrlrComssnInd> [0..1] Indicator 5025
   Role <Role> [0..1] ± 5025
   PrimaryCommunicationAddress <PmryComAdr> [0..*] ± 5025
   SecondaryCommunicationAddress <ScndryComAdr> [0..*] ± 5026
   NameAndAddress <NmAndAdr> [0..1] ± 5026
66.1.30.17  ContactAttributes6
Definition: Communication device number or address used for communication.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4964
   PostalAddress <PstlAdr> [0..1] ± 4964
   PhoneNumber <PhneNb> [0..1] Text 4965
   FaxNumber <FaxNb> [0..1] Text 4965
   EmailAddress <EmailAdr> [0..1] Text 4965
   URLAddress <URLAdr> [0..1] Text 4965
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 4965
   LEI <LEI> [0..1] IdentifierSet 4966
66.1.30.17.1  Name <Nm>
Presence: [0..1]
Definition: Name of the party.
Datatype: "Max350Text" on page 5403
66.1.30.17.2  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4964 May 2026
```

