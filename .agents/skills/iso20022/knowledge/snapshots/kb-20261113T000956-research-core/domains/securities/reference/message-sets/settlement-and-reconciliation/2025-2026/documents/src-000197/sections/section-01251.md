---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.1 PriceInformation30", "35.1.20.1.5 QuotationDate <QtnDt>"]
file_pages: [1708]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.1.5 QuotationDate <QtnDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1708 to 1708.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1708

```text
SourceOfPrice <SrcOfPric> contains the following elements (see "MarketIdentification98" on
page 1523 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1524
   Type <Tp> [1..1]  1524
{Or     Code <Cd> [1..1] CodeSet 1524
Or}     Proprietary <Prtry> [1..1] ± 1525
Constraints
• SmartContractAutomatedPricingRule
When Type/Code does not equal SmartContractAutomatedPricingSystem (SCAS) then Identification/
Description length must be maximum 35 characters.
35.1.20.1.5  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.20.2  TypeOfPrice48Choice
Definition: Choice of formats for a type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1708
Or}   Proprietary <Prtry> [1..1] ± 1709
35.1.20.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice17Code" on page 2175
CodeName Name Definition
BIDE Bid Price is the calculated bid price of a
dual-priced fund (offer-bid prices), that
is, the selling price of the units for the
investor.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1708 March 2026
```

