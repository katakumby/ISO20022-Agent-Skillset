---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.14 ChargeDetails <ChrgDtls>", "13.4.9.14.14.1 Type <Tp>", "13.4.9.14.14.1.1 Code <Cd>"]
file_pages: [195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.14.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 195 to 195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 195

```text
Type <Tp> contains one of the following ChargeType11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 195
Or}   Proprietary <Prtry> [1..1] Text 195
13.4.9.14.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Charge type expressed as an ISO 20022 code.
Datatype: "ChargeType9Code" on page 5283
CodeName Name Definition
MANF ManagementFee Fee paid to an investment manager for
services. The fee usually includes fund
administration costs and investor
relationship management. Typically, the
amount paid is a percentage of the
assets under management.
BEND BackEndLoad Sales charge paid by the investor when
redeeming an investment such as an
investment fund.
FEND FrontEndLoad Sales charge paid immediately by the
investor when subscribing to an
investment such as an investment fund.
ADVI AdvisoryFee Fee paid for advisory services rendered.
CUST CustodyFee Fee paid to a custodian in respect of
custodial services.
PUBL PublicationFee Fee paid in respect of publications
made.
ACCT AccountingFee Fee paid for accounting services
rendered.
EQUL Equalisation The part of an investor's subscription
amount that is held by the fund in order
to pay incentive or performance fees at
the end of the fiscal year.
PENA Penalty Fee charged to the investor for early
redemption of the fund.
13.4.9.14.14.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Charge type expressed as an extended code.
Datatype: "Max350Text" on page 5403
13.4.9.14.14.2  ChargesFees <ChrgsFees>
Presence: [1..1]
Definition: Amount of money asked or paid for the charge.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 195 May 2026
```

