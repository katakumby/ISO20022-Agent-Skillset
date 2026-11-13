---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Securities account position response"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.040.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P923-P928; XML P931-P1045"}, {"source_id": "src-000374", "locator": "Word file/printed pages45,46,47"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000318", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Securities account position response

[src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P923-P928; XML P931-P1045.

**P923** Description

**P924** In this example T2S sends a Securities Account Position Response containing 3 restriction references matching the query criteria specified in the query with reference “MSG700”, which is requesting the current day positions related to the Restriction Type “BLK1” within securities account “1000000123”. The securities positions returned in respond to the query are the current day positions at 09:30:47 with the following details:

**P925** Securities account “1000000123” with 4000 “ISIN00000002” blocked (not available) at BLK1.

**P926** – 1000 units with restriction reference 98586776475.

**P927** – 1000 units with restriction reference 98745787450.

**P928** – 2000 units with restriction reference 1234767634.

```xml
<SctiesAcctPosRspn>
		<Pgntn>
			<PgNb>1</PgNb>
			<LastPgInd>true</LastPgInd>
		</Pgntn>
		<RptGnlDtls>
			<QryRef>MSG700</QryRef>
			<HstrcData>false</HstrcData>
			<ActvtyInd>true</ActvtyInd>
			<SubAcctInd>false</SubAcctInd>
		</RptGnlDtls>
		<AcctOwnr>
			<Id>
				<AnyBIC>PRTAFRPPXXX</AnyBIC>
			</Id>
		</AcctOwnr>
		<AcctSvcr>
			<Id>
				<AnyBIC>CSDBBIC2XXX</AnyBIC>
			</Id>
		</AcctSvcr>
		<Bals>
			<SfkpgAcct>
				<Id>1000000123</Id>
			</SfkpgAcct>
			<BalForAcct>
				<BalDt>
					<DtTm>2025-09-12T09:30:47.000</DtTm>
				</BalDt>
				<FinInstrmId>
					<ISIN>ISIN00000002</ISIN>
				</FinInstrmId>
				<NotAvlblBal>
					<Qty>
						<Unit>4000</Unit>
					</Qty>
				</NotAvlblBal>
				<BalBrkdwn>
					<SubBalTp>
						<Prtry>
							<Id>BLCK</Id>
							<Issr>T2S</Issr>
							<SchmeNm>RPT</SchmeNm>
						</Prtry>
					</SubBalTp>
					<Qty>
						<Qty>
							<Qty>
								<Unit>4000</Unit>
							</Qty>
						</Qty>
					</Qty>
					<AddtlBalBrkdwnDtls>
						<SubBalTp>
							<Prtry>
								<Id>BLK1</Id>
								<Issr>T2S</Issr>
								<SchmeNm>RT</SchmeNm>
							</Prtry>
						</SubBalTp>
						<Qty>
							<Qty>
								<Qty>
									<Unit>4000</Unit>
								</Qty>
							</Qty>
						</Qty>
						<SubBalAddtlDtls>Blocked restriction type 1</SubBalAddtlDtls>
						<QtyBrkdwn>
							<LotNb>
								<Id>98586776475</Id>
							</LotNb>
							<LotQty>
								<Qty>
									<Qty>
										<Qty>
											<Unit>1000</Unit>
										</Qty>
									</Qty>
								</Qty>
							</LotQty>
						</QtyBrkdwn>
						<QtyBrkdwn>
							<LotNb>
								<Id>98745787450</Id>
							</LotNb>
							<LotQty>
								<Qty>
									<Qty>
										<Qty>
											<Unit>1000</Unit>
										</Qty>
									</Qty>
								</Qty>
							</LotQty>
						</QtyBrkdwn>
						<QtyBrkdwn>
							<LotNb>
								<Id>1234767634</Id>
							</LotNb>
							<LotQty>
								<Qty>
									<Qty>
										<Qty>
											<Unit>2000</Unit>
										</Qty>
									</Qty>
								</Qty>
							</LotQty>
						</QtyBrkdwn>
					</AddtlBalBrkdwnDtls>
				</BalBrkdwn>
			</BalForAcct>
		</Bals>
	</SctiesAcctPosRspn>
```

## Review and validation

All source example pages compared2026-11-09: [45](../../../../../../../evidence/omitted/3514e22d53e63969c2d9fcbd.md), [46](../../../../../../../evidence/omitted/efe246d0a0334f8bd2f9b6d2.md), [47](../../../../../../../evidence/omitted/9d2cec344ebbef0db4c9aebf.md). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
