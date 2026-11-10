---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.1 SourceOfCash1Choice", "66.1.31.1.2 Proprietary <Prtry>"]
file_pages: [5046]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5046 to 5046.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5046

```text
CodeName Name Definition
REPY RetirementPolicy Income from a retirement policy.
SEAQ SaleAquisitionCorporation Sale and acquisition of a corporation.
SALE SaleOfGoods Sale of goods.
SVGS Savings Income from a savings plan.
SELF SelfEmploymentIncome Income from self-employment.
WINS Winnings Income from a cash win.
66.1.31.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Source of cash expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.31.2  PaymentCard29
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 5046
   Number <Nb> [1..1] Text 5047
   HolderName <HldrNm> [1..1] Text 5047
   StartDate <StartDt> [0..1] YearMonth 5047
   ExpiryDate <XpryDt> [1..1] YearMonth 5047
   CardIssuerName <CardIssrNm> [0..1] Text 5047
   CardIssuerIdentification <CardIssrId> [0..1] ± 5047
   SecurityCode <SctyCd> [0..1] Text 5048
   SequenceNumber <SeqNb> [0..1] Text 5048
66.1.31.2.1  Type <Tp>
Presence: [1..1]
Definition: Type of card, for example, credit card.
Datatype: "CardType1Code" on page 5281
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5046 May 2026
```

