---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.13 Standardisation <Stdstn>", "13.1.2.2.2.13.2 Proprietary <Prtry>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.13.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
CodeName Name Definition
instruments, expiration date and contract
size of the derivatives are not
standardised.
STAN Standardised The underlying instruments, expiration
date and contract size of the derivatives
are standardised.
13.1.2.2.2.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Standardisation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.2.14  TradingPartyRole <TradgPtyRole>
Presence: [0..1]
Definition: Specifies the party which is the buyer or the seller.
TradingPartyRole <TradgPtyRole> contains one of the following OptionParty3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 184
Or}   Proprietary <Prtry> [1..1] ± 184
13.1.2.2.2.14.1  Code <Cd>
Presence: [1..*]
Definition: Option party expressed as an ISO 20022 code.
Datatype: "OptionParty1Code" on page 520
CodeName Name Definition
SLLR Seller Seller in a trade.
BYER Buyer Buyer in a trade.
13.1.2.2.2.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option party expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 184 March 2024
```

