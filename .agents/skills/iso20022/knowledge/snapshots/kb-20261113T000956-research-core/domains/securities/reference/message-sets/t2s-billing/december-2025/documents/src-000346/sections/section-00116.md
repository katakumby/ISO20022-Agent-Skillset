---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.9 Postal Address", "4.1.9.3 NameAndAddress5", "4.1.9.3.2 Address <Adr>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.9.3.2 Address <Adr>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
4.1.9.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 140
   AddressLine <AdrLine> [0..5] Text 140
   StreetName <StrtNm> [0..1] Text 140
   BuildingNumber <BldgNb> [0..1] Text 140
   PostCode <PstCd> [0..1] Text 141
   TownName <TwnNm> [0..1] Text 141
   CountrySubDivision <CtrySubDvsn> [0..1] Text 141
   Country <Ctry> [1..1] CodeSet C3 141
4.1.10 System Identification
4.1.10.1  SystemIdentification2Choice
Definition: Information used to identify a cash clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 142
Or}   Country <Ctry> [1..1] CodeSet C3 142
4.1.10.1.1  MarketInfrastructureIdentification <MktInfrstrctrId>
Presence: [1..1]
Definition: Clearing service selected for a transaction.
MarketInfrastructureIdentification <MktInfrstrctrId> contains one of the following elements (see
"MarketInfrastructureIdentification1Choice" on page 121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 121
Or}   Proprietary <Prtry> [1..1] Text 121
4.1.10.1.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which the system is located.
Impacted by: C3 "Country"
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 142 December 2025
```

