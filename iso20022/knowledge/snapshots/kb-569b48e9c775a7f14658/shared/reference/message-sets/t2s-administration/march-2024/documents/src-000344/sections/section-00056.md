---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.10 System Identification", "5.1.10.1 ClearingSystemIdentification2Choice", "5.1.10.1.2 Proprietary <Prtry>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.10.1.2 Proprietary <Prtry>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
Datatype: "ExternalClearingSystemIdentification1Code" on page 64
5.1.10.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 69
5.2 Message Datatypes
5.2.1 CodeSet
5.2.1.1  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
5.2.1.2  BalanceCounterparty1Code
Definition: Specifies the type of counterparty to be taken into account for calculation of the balance.
Type: CodeSet
CodeName Name Definition
BILA Bilateral Balance calculated regarding one
member in the system.
MULT Multilateral Balance calculated regarding all
members in the system.
5.2.1.3  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
63 March 2024
```

