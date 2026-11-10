---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["11 camt.012.001.08 DeleteLimitV08", "11.4 Message Building Blocks", "11.4.2 LimitDetails <LmtDtls>", "11.4.2.1 CurrentLimitIdentification <CurLmtId>", "11.4.2.1.1 SystemIdentification <SysId>"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.012.001.08"]
---

# 11.4.2.1.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
Constraints
• BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
On Condition
    /Type/Code is equal to value 'Multilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be absent
• BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
On Condition
    /Type/Code is equal to value 'Bilateral'
 Or    /Type/Code is equal to value 'NetBilateral'
 Or    /Type/Code is equal to value 'IndirectBilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be present
11.4.2.1.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
11.4.2.1.2  BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId>
Presence: [0..1]
Definition: Identification of the system member for which the limit is established.
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 454 February 2025
```

