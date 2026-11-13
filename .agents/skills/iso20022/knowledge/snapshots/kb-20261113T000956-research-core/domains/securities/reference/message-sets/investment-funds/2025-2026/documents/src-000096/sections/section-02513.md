---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.8 RelatedPartyDetails <RltdPtyDtls>", "53.4.5.8.2 Account <Acct>", "53.4.5.8.2.1 Identification <Id>"]
file_pages: [3541]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.8.2.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3541 to 3541.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3541

```text
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Account <Acct> contains the following Account35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3541
   AccountServicer <AcctSvcr> [0..1] ± 3541
53.4.5.8.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
53.4.5.8.2.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Institution servicing the account and assigning the account identifier to the account owner.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.8.3  OrderOriginatorEligibility <OrdrOrgtrElgblty>
Presence: [0..1]
Definition: Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to
transactions executed by investment firms for eligible counterparties.
Datatype: "OrderOriginatorEligibility1Code" on page 5332
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3541 May 2026
```

